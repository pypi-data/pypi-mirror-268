import os
import sys
import typing as t
from pathlib import Path

if "flask" in sys.modules:
    from flask import Flask, url_for, send_from_directory
    from markupsafe import Markup
else:
    raise ImportError("Flask is not installed.")

from vite_transporter._html_tags import BodyContent, ScriptTag, LinkTag
from vite_transporter.helpers import Colr


class ViteTransporter:
    app: t.Optional[Flask]
    vt_root_path: Path

    cors_allow_all: bool

    def __init__(
        self, app: t.Optional[Flask] = None, cors_allow_all: t.Optional[bool] = None
    ) -> None:
        if app is not None:
            self.init_app(app, cors_allow_all)

    def init_app(self, app: Flask, cors_allow_all: t.Optional[bool] = None) -> None:
        if app is None:
            raise ImportError("No app was passed in.")
        if not isinstance(app, Flask):
            raise TypeError("The app that was passed in is not an instance of Flask")

        self.app = app
        self.cors_allow_all = cors_allow_all or os.getenv("VT_CORS_ALLOW_ALL", False)

        print(self.cors_allow_all)

        if "vite_transporter" in self.app.extensions:
            raise ImportError(
                "The app has already been initialized with vite-to-flask."
            )

        self.app.extensions["vite_transporter"] = self
        self.app.config["VTF_APPS"] = {}
        self.vt_root_path = Path(app.root_path) / "vt"

        if not self.vt_root_path.exists():
            raise FileNotFoundError(
                "vt directory not found in the flask app root directory."
            )

        for folder in self.vt_root_path.iterdir():
            if folder.is_dir():
                self.app.config["VTF_APPS"].update({folder.name: folder})

        self._load_routes(app)
        self._load_context_processor(app)
        self._load_cors_headers(app, self.cors_allow_all)

    def _load_routes(self, app: Flask) -> None:
        @app.route("/__vt/<vite_app>/<filename>")
        def __vt(vite_app: str, filename: str):
            return send_from_directory(self.vt_root_path / vite_app, filename)

    @staticmethod
    def _load_context_processor(app: Flask) -> None:
        @app.context_processor
        def vt_head_processor():
            def vt_head(vite_app: str) -> t.Any:
                vite_assets = Path(app.root_path) / "vt" / vite_app
                find_vite_js = vite_assets.glob("*.js")
                find_vite_css = vite_assets.glob("*.css")

                tags = []

                for file in find_vite_js:
                    print("found", file)
                    tags.append(
                        ScriptTag(
                            src=url_for("__vt", vite_app=vite_app, filename=file.name),
                            type_="module",
                        )
                    )

                for file in find_vite_css:
                    print("found", file)
                    tags.append(
                        LinkTag(
                            rel="stylesheet",
                            href=url_for("__vt", vite_app=vite_app, filename=file.name),
                        )
                    )

                return Markup("".join([tag.raw() for tag in tags]))

            return dict(vt_head=vt_head)

        @app.context_processor
        def vt_body_processor():
            def vt_body(
                root_id: str = "root",
                noscript_message: str = "You need to enable JavaScript to run this app.",
            ) -> t.Any:
                return BodyContent(root_id, noscript_message)()

            return dict(vt_body=vt_body)

    @staticmethod
    def _load_cors_headers(app: Flask, cors_allow_all: bool = False) -> None:
        if cors_allow_all:
            print(
                f"{Colr.WARNING}{Colr.BOLD}vite-transporter is disabling CORS restrictions."
                f"{Colr.END}{Colr.END}\n\r"
                f"{Colr.OKCYAN}Access-Control-Allow-Origin set to '*' {Colr.END}\n\r"
                f"{Colr.OKCYAN}Access-Control-Allow-Headers set to '*' {Colr.END}\n\r"
                f"{Colr.OKCYAN}Access-Control-Allow-Methods set to '*' {Colr.END}\n\r"
                f"{Colr.WARNING}{Colr.BOLD}Remember to disable this in production!{Colr.END}{Colr.END}"
            )

            @app.after_request
            def after_request(response):
                response.headers["Access-Control-Allow-Origin"] = "*"
                response.headers["Access-Control-Allow-Headers"] = "*"
                response.headers["Access-Control-Allow-Methods"] = "*"
                return response

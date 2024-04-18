from dotenv import load_dotenv
from quart import Quart, render_template

from vite_transporter.platform.quart import ViteTransporter

load_dotenv()


def create_app():
    app = Quart(__name__)
    ViteTransporter(app, cors_allow_all=True)

    @app.route("/")
    async def index():
        return await render_template("index.html")

    return app


def run():
    # used for pyqwe
    _app = create_app()
    _app.run(port=5000, debug=True)

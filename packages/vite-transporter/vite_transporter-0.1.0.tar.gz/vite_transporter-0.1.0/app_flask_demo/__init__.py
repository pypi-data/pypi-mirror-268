from dotenv import load_dotenv
from flask import Flask, render_template

from vite_transporter.platform.flask import ViteTransporter

load_dotenv()


def create_app():
    app = Flask(__name__)
    ViteTransporter(app, cors_allow_all=True)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app


def run():
    # used for pyqwe
    _app = create_app()
    _app.run(port=5001, debug=True)

import os
from flask import Flask
from config import get_config
from routes.main_routes import main_bp


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(get_config())
    app.register_blueprint(main_bp)
    return app


if __name__ == "__main__":
    create_app().run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", "5001")),
        debug=True,
    )
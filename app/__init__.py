from flask import Flask
from .config import Config
from .db import init_db
from .views.livros import livros_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(livros_bp)

    init_db(app)

    return app

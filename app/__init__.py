from flask import Flask
from .config import Config
from .db import db
from .views.livros import livros_bp
from .views.users import users_bp
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(livros_bp)
    app.register_blueprint(users_bp)

    db.init_app(app)
    migrate = Migrate(app, db)

    return app

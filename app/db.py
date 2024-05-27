from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    from .models.livros import Livro

    db.init_app(app)
    # with app.app_context():
    #     db.create_all()



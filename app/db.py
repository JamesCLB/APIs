from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    from .models.livros import Livro

    # with app.app_context():
    #     db.create_all()



from app.db import db


class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Book: {self.title}"

    def to_json(self):
        return {"id": self.id, "title": self.title, "author": self.author, "published_date": self.published_date}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    year_of_birth = db.Column(db.String(10), nullable=False)

    def to_json(self):
        return {"id": self.id, "user_name": self.user_name, "password": self.password,
                "year_of_birth": self.year_of_birth}

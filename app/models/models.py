from app.db import db

user_books = db.Table("user_books",
                      db.Column("user_id", db.Integer, db.ForeignKey("user.id"), primary_key=True),
                      db.Column('book_id', db.Integer, db.ForeignKey('livro.id'), primary_key=True)
                      )


class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    author = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Book: {self.title}"

    def to_json(self):
        return {"id": self.id, "title": self.title, "author": self.author, "published_date": self.published_date,
                "users": [user.to_json() for user in self.users.all()]}


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    books = db.relationship("Livro", secondary=user_books, lazy="dynamic", backref=db.backref("users", lazy=True))

    def to_json(self):
        return {"id": self.id, "user_name": self.user_name, "password": self.password,
                "books": [book.to_json() for book in self.books.all()]}

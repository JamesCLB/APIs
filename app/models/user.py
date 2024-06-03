from app.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    year_of_birth = db.Column(db.String(10), nullable=False)

    def to_json(self):
        return {"id": self.id, "user_name": self.user_name, "password": self.password,
                "year_of_birth": self.year_of_birth}

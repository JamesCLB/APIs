from ..models.models import Livro, User, user_books
from ..controllers import gera_response
from flask import jsonify

"""def user_book_json(user_book):
    return {"user":}"""


def add_user_book(user_id, session, body):
    book_id = body["id"]
    user_obj = User.query.filter_by(id=user_id).first()
    book_obj = Livro.query.filter_by(id=book_id).first()
    if not user_obj or not book_obj:
        return gera_response(400, "user_books", {}, "book and user required")

    user_obj.books.append(book_obj)
    session.commit()

    return gera_response(200, "user_books", user_obj.to_json(), "book added to user")


def get_user_books(session):
    user_books_obj = session.execute(user_books.select()).fetchall()
    user_books_json = []
    for user_book in user_books_obj:
        user_books_json.append({"user": user_book.user_id, "book": user_book.book_id})

    return jsonify(user_books_json)



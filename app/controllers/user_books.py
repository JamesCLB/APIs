from ..models.models import Livro, User, user_books
from ..controllers import gera_response
from flask import jsonify


def user_book_to_json(user_book):
    if user_book:
        return {"user_id": user_book.user_id, "book_id": user_book.book_id, "status": user_book.status}
    else:
        return None


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
        user_books_json.append(user_book_to_json(user_book))

    return jsonify(user_books_json)


def upd_user_book(session, user_id, book_id, body):
    try:
        user_book_obj = session.execute(
            user_books.select().where(
                user_books.c.user_id == user_id,
                user_books.c.book_id == book_id
            )
        ).first()

        if not user_book_obj:
            return gera_response(404, "user_book", {}, "user book not found")

        if "status" in body:
            session.execute(
                user_books.update().where(
                    user_books.c.user_id == user_id,
                    user_books.c.book_id == book_id
                ).values(status=body["status"])
            )
            session.commit()

        return gera_response(200, "user_book", user_book_to_json(user_book_obj), "book status updated")

    except Exception as e:
        print(e)
        return gera_response(400, "user_book", {}, "error to update the user_book")


from ..models.models import Livro, User, user_books
from ..controllers import gera_response
from app.db import db


def user_book_to_json(user_book):
    if user_book:
        return {"user_id": user_book.user_id, "book_id": user_book.book_id, "status": user_book.status}
    else:
        return None


def take_user_books(user_id):
    user_obj = User.query.filter(User.id == user_id).first()
    books_json = [book.to_json() for book in user_obj.books]

    return gera_response(200, "books", books_json, "books")


def add_user_book(user_id, session, body):
    try:
        book_id = body["ids"]
        user_obj = User.query.filter_by(id=user_id).first()
        book_objs = Livro.query.filter(Livro.id.in_(book_id))
        if not user_obj or not book_objs:
            return gera_response(400, "user_books", {}, "book and user required")

        for book in book_objs:
            if book not in user_obj.books:
                user_obj.books.append(book)

        session.commit()
    except Exception as e:
        print(e)
        return gera_response(400, "user_books", {}, "Error to add the book to user")
    return gera_response(200, "user_books", user_obj.to_json(), "Books added to user")


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

        user_book_obj = session.execute(
            user_books.select().where(
                user_books.c.user_id == user_id,
                user_books.c.book_id == book_id
            )
        ).first()

        return gera_response(200, "user_book", user_book_to_json(user_book_obj), "book status updated")
    except Exception as e:
        print(e)
        return gera_response(400, "user_book", {}, "error to update the user_book")


def delete_user_book(user_id, book_id):
    session = db.session
    session.query(user_books).filter(
        user_books.c.user_id == user_id,
        user_books.c.book_id == book_id
    ).delete()

    return gera_response(200, "user_book", {}, "user book deleted")

from ..models.models import Livro, User, user_books
from ..controllers import gera_response


def add_user_book(user_id, book_id, session):
    user_obj = User.query.filter_by(id=user_id).first()
    book_obj = Livro.query.filter_by(id=book_id).first()
    if not user_obj or not book_obj:
        return gera_response(400, "user_books", {}, "book and user required")

    user_obj.books.append(book_obj)
    session.commit()

    return gera_response(200, "user_books", user_obj.to_json(), "book added to user")


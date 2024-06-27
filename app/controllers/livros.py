from flask import jsonify, abort
from ..models.models import Livro, User
from . import gera_response


def take_book(id_book):

    book = Livro.query.filter_by(id=id_book).first()

    if not book:
        abort(404, gera_response("404", "book", {}, f"book with id {id_book} not found"))
    return book


def take_all_books():
    books_obj = Livro.query.all()
    books_json = [book.to_json() for book in books_obj]

    return jsonify(books_json)


def create_book(body, session):
    try:
        if "title" not in body:
            return gera_response(400, "book", {}, "title required")
        title = body["title"]
        if "author" not in body:
            return gera_response(400, "book", {}, "author required")
        author = body["author"]
        if "published_date" not in body:
            return gera_response(400, "book", {}, "published date required")
        published_date = body["published_date"]

        if title.strip() == "":
            return gera_response("400", "book", {}, "title required")

        book_exist = Livro.query.filter_by(title=title).first()
        if book_exist:
            return gera_response(400, "book", {}, f"error, the book {title} already exist")
        new_book = Livro(title=title, author=author, published_date=published_date)

        session.add(new_book)
        session.commit()

        return gera_response(200, "livro", new_book.to_json(), "book added")

    except Exception as e:
        print(e)
        return gera_response(400, "livro", {}, "error to add the book")


def delete_book(id_book, session):
    try:
        book = take_book(id_book)

        session.delete(book)
        session.commit()

        return gera_response(200, "livro", book.to_json(), "Livro deletado")
    except Exception as e:
        print(e)
        return gera_response(400, "livro", {}, "Erro ao deletar o livro")


def upd_book(id_book, session, body):
    try:
        book_obj = take_book(id_book)
        if "title" in body:
            book_obj.title = body["title"]
        if "author" in body:
            book_obj.author = body["author"]
        if "published_date" in body:
            book_obj.published_date = body["published_date"]

        session.commit()

        return gera_response(200, "livro", book_obj.to_json(), "Livro atualizado")
    except Exception as e:
        print(e)
        return gera_response(400, "livro", {}, "Erro ao atualizar o livro")
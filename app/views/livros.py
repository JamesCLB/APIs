from flask import request, Blueprint
from app.db import db
from ..controllers.livros import take_book, take_all_books, create_book, delete_book, upd_book

livros_bp = Blueprint("livros", __name__, url_prefix="/books")


@livros_bp.route("/", methods=["GET"])
def get_books_route():
    return take_all_books()


@livros_bp.route("/<id_book>", methods=["GET"])
def get_book_route(id_book):
    book = take_book(id_book)

    if isinstance(book, tuple):
        return book

    return take_book(id_book).to_json()


@livros_bp.route("", methods=["POST"])
def create_book_route():
    body = request.get_json()
    session = db.session
    return create_book(body, session)


@livros_bp.route("/<id_book>", methods=["DELETE"])
def delete_book_route(id_book):
    session = db.session
    return delete_book(id_book, session)


@livros_bp.route("/<id_book>", methods=["PUT"])
def put_book_route(id_book):
    body = request.get_json()
    session = db.session
    return upd_book(id_book, session, body)




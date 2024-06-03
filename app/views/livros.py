from flask import request, Response, jsonify, Blueprint
from ..models.models import Livro, User
from app.db import db
from ..controllers.livros import gera_response, take_book, take_all_books, create_book, delete_book, upd_book

livros_bp = Blueprint("livros", __name__)


@livros_bp.route("/books", methods=["GET"])
def get_books_route():
    return take_all_books()


@livros_bp.route("/book/<id_book>", methods=["GET"])
def get_book_route(id_book):
    return take_book(id_book).to_json()


@livros_bp.route("/book", methods=["POST"])
def create_book_route():
    body = request.get_json()
    session = db.session
    return create_book(body, session)


@livros_bp.route("/book/<id_book>", methods=["DELETE"])
def delete_book_route(id_book):
    session = db.session
    return delete_book(id_book, session)


@livros_bp.route("/book/<id_book>", methods=["PUT"])
def att_book_route(id_book):
    body = request.get_json()
    session = db.session
    return upd_book(id_book, session, body)




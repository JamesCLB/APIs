from flask import Blueprint, request
from ..controllers.user_books import add_user_book, get_user_books, upd_user_book, delete_user_book
from ..db import db

user_books_bp = Blueprint("user_books", __name__, url_prefix="/user_books")


@user_books_bp.route("/add/<int:user_id>/book", methods=["POST"])
def add_user_book_route(user_id):
    body = request.get_json()
    return add_user_book(user_id, db.session, body)


@user_books_bp.route("/", methods=["GET"])
def get_user_books_route():
    session = db.session
    return get_user_books(session)


@user_books_bp.route("/user/<int:id_user>/book/<int:id_book>", methods=["PUT"])
def put_user_book_route(id_user, id_book):
    session = db.session
    body = request.get_json()
    return upd_user_book(session, id_user, id_book, body)


@user_books_bp.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user_book_route(user_id):
    body = request.get_json()
    session = db.session
    return delete_user_book(user_id, body, session)

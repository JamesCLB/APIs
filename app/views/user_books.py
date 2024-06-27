from flask import Blueprint, request
from ..controllers.user_books import add_user_book, upd_user_book, delete_user_book, take_user_books
from ..db import db


user_books_bp = Blueprint("user_books", __name__, url_prefix="/users")


@user_books_bp.route("/<int:user_id>/books", methods=["POST"])
def add_user_books_route(user_id):
    body = request.get_json()
    return add_user_book(user_id, db.session, body)


@user_books_bp.route("/<int:user_id>/books", methods=["GET"])
def get_user_books_route(user_id):
    return take_user_books(user_id)


@user_books_bp.route("/<int:id_user>/books/<int:id_book>", methods=["PUT"])
def put_user_book_route(id_user, id_book):
    session = db.session
    body = request.get_json()
    return upd_user_book(session, id_user, id_book, body)


@user_books_bp.route("/<int:user_id>/books/<int:id_book>", methods=["DELETE"])
def delete_user_book_route(user_id, id_book):
    return delete_user_book(user_id, id_book)

from flask import Blueprint, request
from ..controllers.user_books import add_user_book, get_user_books
from ..db import db

user_books_bp = Blueprint("user_books", __name__, url_prefix="/user_books")


@user_books_bp.route("/add/<user_id>/book", methods=["POST"])
def add_user_book_route(user_id):
    body = request.get_json()
    return add_user_book(user_id, db.session, body)


@user_books_bp.route("/", methods=["GET"])
def get_user_books_route():
    session = db.session
    return get_user_books(session)






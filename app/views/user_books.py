from flask import Blueprint, request
from ..controllers.user_books import add_user_book
from ..db import db

user_books_bp = Blueprint("user_books", __name__, url_prefix="user_books")


@user_books_bp.route("/add", methods=["POST"])
def add_user_book_route(user_id, book_id):
    return add_user_book(user_id, book_id, db.session, request)

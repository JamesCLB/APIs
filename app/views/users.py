from flask import request, Blueprint, jsonify
from app.db import db
from ..models.models import User
from ..controllers.users import take_all_users, create_user, delete_user

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def get_users_route():
    return take_all_users()


@users_bp.route("/user", methods=["POST"])
def create_user_route():
    body = request.get_json()
    session = db.session

    return create_user(body, session)


@users_bp.route("/user/<id_user>", methods=["DELETE"])
def delete_user_route(id_user):
    session = db.session

    return delete_user(id_user, session)


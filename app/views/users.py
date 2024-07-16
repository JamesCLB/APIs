from flask import request, Blueprint
from app.db import db
from app.controllers.users import take_all_users, create_user, delete_user, upd_user, take_user
from app.controllers import validate_schema
from app.jsonschema.schemas import user_schema

users_bp = Blueprint("users", __name__)


@users_bp.route("/user/<id_user>", methods=["GET"])
def get_user_route(id_user):
    user = take_user(id_user)
    if isinstance(user, tuple):
        return user
    return take_user(id_user).to_json()


@users_bp.route("/users", methods=["GET"])
def get_users_route():
    return take_all_users()


@users_bp.route("/user", methods=["POST"])
@validate_schema(user_schema)
def create_user_route():
    body = request.get_json()
    session = db.session

    return create_user(body, session)


@users_bp.route("/user/<id_user>", methods=["DELETE"])
def delete_user_route(id_user):
    session = db.session

    return delete_user(id_user, session)


@users_bp.route("/user/<id_user>", methods=["PUT"])
def put_user_route(id_user):
    session = db.session
    body = request.get_json()
    return upd_user(id_user, body, session)


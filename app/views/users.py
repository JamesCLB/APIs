from flask import request, Blueprint, jsonify
from app.db import db
from ..models.models import User

users_bp = Blueprint("users", __name__)


@users_bp.route("/users", methods=["GET"])
def get_users_route():
    users_class = User.query.all()
    users_json = [user.to_json() for user in users_class]

    return jsonify(users_json)

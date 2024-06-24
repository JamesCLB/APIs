from flask import jsonify
from ..models.models import User
from . import gera_response


def take_user(id_user):
    user = User.query.filter_by(id=id_user).first()
    return user


def take_all_users():
    users_obj = User.query.all()
    users_json = [user.to_json() for user in users_obj]

    return jsonify(users_json)


def create_user(body, session):
    try:
        if "user_name" not in body or body["user_name"].strip() == "":
            return gera_response(400, "user", {}, "user name required")
        user_name = body["user_name"]
        if "password" not in body or body["password"].strip() == "":
            return gera_response(400, "user", {}, "password required")
        password = body["password"]

        user_exist = User.query.filter_by(user_name=user_name).first()

        if user_exist:
            return gera_response(400, "user", {}, "username already used")

        new_user = User(user_name=user_name, password=password)

        session.add(new_user)
        session.commit()

        return gera_response(200, "user", new_user.to_json(), "user added")

    except Exception as e:
        print(e)
        return gera_response(400, "user", {}, "error to add the user")


def delete_user(id_user, session):
    try:
        user = User.query.filter_by(id=id_user).first()

        session.delete(user)
        session.commit()

        return gera_response(200, "user", user.to_json(), "user deleted")
    except Exception as e:
        print(e)
        return gera_response(400, "user", {}, "error to delete the user")


def upd_user(id_book, body, session):
    try:
        user_obj = take_user(id_book)
        if "id" in body:
            user_obj.user_id = body["id"]
        if "user_name" in body:
            user_obj.user_name = body["user_name"]
        if "password" in body:
            user_obj.password = body["password"]

        session.commit()

        return gera_response(200, "user", user_obj.to_json(), "User updated")
    except Exception as e:
        print(e)
        return gera_response(400, "user", {}, "error to update the user")


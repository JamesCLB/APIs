from functools import wraps
from flask import jsonify, request
from jsonschema import validate, ValidationError


def gera_response(status, name_content, content=None, msg=""):
    body = {name_content: content}

    if msg:
        body["mensagem"] = msg

    return jsonify(body), status


def validate_schema(schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            body = request.get_json()
            try:
                validate(instance=body, schema=schema)
            except ValidationError as e:
                return gera_response(400, "validation_error", {}, f"validation error: {e.message}")
            return f(*args, **kwargs)
        return decorated_function
    return decorator

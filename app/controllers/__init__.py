from flask import jsonify


def gera_response(status, name_content, content=None, msg=""):
    body = {name_content: content}

    if msg:
        body["mensagem"] = msg

    return jsonify(body), status

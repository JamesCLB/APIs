from flask import jsonify
from ..models.livros import Livro


def gera_response(status, name_content, content=None, msg=""):
    body = {name_content: content}

    if msg:
        body["mensagem"] = msg

    return jsonify(body), status


def take_book(id_book):
    book = Livro.query.filter_by(id=id_book).first()
    return book

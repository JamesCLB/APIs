from flask import request, Response, jsonify, Blueprint
from ..models.livros import Livro
from app.db import db
from ..controllers.livros import gera_response, take_book, take_all_books

livros_bp = Blueprint("livros", __name__)


@livros_bp.route("/books", methods=["GET"])
def get_bookss():
    return take_all_books()


@livros_bp.route("/book", methods=["POST"])
def create_book():
    body = request.get_json()

    try:
        if "title" not in body:
            return gera_response(400, "livro", {}, "Titulo obrigatorio")
        title = body["title"]
        if "author" not in body:
            return gera_response(400, "livro", {}, "Autor obrigatorio")
        author = body["author"]
        if "published_date" not in body:
            return gera_response(400, "livro", {}, "Data de publicacao obrigatorio")
        published_date = body["published_date"]

        novo_livro = Livro(title=title, author=author, published_date=published_date)

        db.session.add(novo_livro)
        db.session.commit()

        return gera_response(200, "livro", novo_livro.to_json(), "livro adicionado")
    except Exception as e:
        print(e)
        return gera_response(400, "livro", {}, "Erro ao adicionar o livro")


@livros_bp.route("/book/<id_book>", methods=["DELETE"])
def delete_book(id_book):
    try:
        book = take_book(id_book)

        db.session.delete(book)
        db.session.commit()

        return gera_response(200, "livro", book.to_json(), "Livro deletado")
    except Exception as e:
        print(e)
        return gera_response(400, "livro", {}, "Erro ao deletar o livro")


@livros_bp.route("/book/<id_book>", methods=["PUT"])
def att_book(id_book):
    body = request.get_json()
    try:
        book_obj = take_book(id_book)
        if "title" in body:
            book_obj.title = body["title"]
        if "author" in body:
            book_obj.author = body["author"]
        if "published_date" in body:
            book_obj.published_date = body["published_date"]

        db.session.commit()

        return gera_response(200, "livro", book_obj.to_json(), "Livro atualizado")
    except Exception as e:
        print(e)
        return gera_response(400, "livro", {}, "Erro ao atualizar o livro")




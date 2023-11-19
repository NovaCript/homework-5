from flask import Blueprint, request, jsonify

from app.repositories.configuratebook import ConfigurateBook
from app.repositories.repositories import BookRepository

book_bp = Blueprint('book_bp', __name__, url_prefix='/books')


@book_bp.delete('/<int:id>')
def delete_book(id):
    book = BookRepository.get_book_by_id(id)
    cfg_book = ConfigurateBook.config_delete_book(book)
    return jsonify(cfg_book)


@book_bp.get('/<int:id>')
def get_book(id):
    book = BookRepository.get_book_by_id(id)
    cfg_book = ConfigurateBook.config_book_id(book)
    return jsonify(cfg_book)


@book_bp.get('/')
def get_all_books():
    books = BookRepository.get_all_book()
    cfg_book = ConfigurateBook.config_get_all_books(books)
    return jsonify(cfg_book)


@book_bp.post('/')
def add_book():
    data = request.get_json()
    cfg_book = ConfigurateBook.config_add_book(data)
    return jsonify(cfg_book)


@book_bp.put('/<int:id>')
def update_book(id):
    book = BookRepository.get_book_by_id(id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    data = request.get_json()
    cfg_book = ConfigurateBook.config_update_book(data, book)
    return jsonify(cfg_book)

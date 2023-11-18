from datetime import datetime

from flask import Blueprint, request, jsonify

from app.models.models import db, Book
from app.repositories.repositories import BookRepository

book_bp = Blueprint('book_bp', __name__, url_prefix='/books')


@book_bp.get('/<int:id>')
def get_book(id):
    book = BookRepository.get_book_by_id(id)
    if book:
        book_data = {
            'id': book.id,
            'title': book.title,
            'description': book.description,
            'publish_year': book.publish_year,
            'pages_count': book.pages_count,
            'created_at': book.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify(book_data)
    else:
        return jsonify({'message': 'Book not found'}), 404


@book_bp.get('/')
def get_all_books():
    books = BookRepository.get_all_book()
    books_data = []
    for book in books:
        book_data = {
            'id': book.id,
            'title': book.title,
            'description': book.description,
            'publish_year': book.publish_year,
            'pages_count': book.pages_count,
            'created_at': book.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        books_data.append(book_data)
    return jsonify(books_data)


@book_bp.post('/')
def add_book():
    data = request.get_json()

    title = data.get('title')
    description = data.get('description')
    publish_year = data.get('publish_year')
    pages_count = data.get('pages_count')

    new_book = Book(
        title=title,
        description=description,
        publish_year=publish_year,
        pages_count=pages_count,
        created_at=datetime.utcnow()
    )

    try:
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to add book', 'error': str(e)}), 500

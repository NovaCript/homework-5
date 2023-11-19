from datetime import datetime

from app.models.models import db, Book


class ConfigurateBook:

    @staticmethod
    def config_book_id(book):
        if book:
            book_data = {
                'id': book.id,
                'title': book.title,
                'description': book.description,
                'publish_year': book.publish_year,
                'pages_count': book.pages_count,
                'created_at': book.created_at.strftime('%Y-%m-%d %H:%M:%S')
            }
            return book_data
        else:
            return {'message': 'Book not found'}, 404

    @staticmethod
    def config_delete_book(book):
        if book:
            try:
                db.session.delete(book)
                db.session.commit()
                return {'message': 'Book deleted successfully!'}
            except Exception as e:
                db.session.rollback()
                return {'message': 'Failed to delete book',
                        'error': str(e)}, 500


    @staticmethod
    def config_get_all_books(books):
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
        return books_data


    @staticmethod
    def config_add_book(data):
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
            return {'message': 'Book added successfully!'}
        except Exception as e:
            db.session.rollback()
            return {'message': 'Failed to add book', 'error': str(e)}, 500


    @staticmethod
    def config_update_book(data, book):
        title = data.get('title')
        description = data.get('description')
        publish_year = data.get('publish_year')
        pages_count = data.get('pages_count')

        book.title = title
        book.description = description
        book.publish_year = publish_year
        book.pages_count = pages_count

        try:
            db.session.commit()
            return {'message': 'Book updated successfully!'}
        except Exception as e:
            db.session.rollback()
            return {'message': 'Failed to update book', 'error': str(e)}, 500


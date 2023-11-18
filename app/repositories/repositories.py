from app.models.models import Book


class BookRepository:
    @staticmethod
    def get_book_by_id(book_id):
        return Book.query.get(book_id)

    @staticmethod
    def get_all_book():
        return Book.query.all()

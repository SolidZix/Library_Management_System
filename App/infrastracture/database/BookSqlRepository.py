# application/books/repository.py
from abc import ABC, abstractmethod
from ...domain.books.entities import Books
from ...infrastracture.database.database import Session
from ...infrastracture.database.database_models import Books as DBBook
from datetime import datetime
from ...domain.books.repository import BookRepository

def vo_value(obj):
    return obj.value if hasattr(obj, "value") else obj

class BookSQLRepository(BookRepository):
    def __init__(self):
        self.session = Session()

    def add(self, book: Books):
        db_book = DBBook(
            title=book.title.value if hasattr(book.title, "value") else book.title,
            author=book.author.value if hasattr(book.author, "value") else book.author,
            is_borrowed=book.is_borrowed.value if hasattr(book.is_borrowed, "value") else book.is_borrowed,
            borrowed_date=book.borrowed_date.value if hasattr(book.borrowed_date, "value") else book.borrowed_date,
            borrowed_by=None if book.borrowed_by is None else book.borrowed_by.value    ,
            created_at=book.created_at.value if hasattr(book.created_at, "value") else book.created_at,
            updated_at=book.updated_at.value if hasattr(book.updated_at, "value") else book.updated_at
            )

        self.session.add(db_book)
        self.session.commit()
        self.session.refresh(db_book)
        return db_book

    def get(self, book_id: int):
        return self.session.query(DBBook).filter_by(book_id=book_id).first()

    # LIST ALL BOOKS
    def list(self):
        results = self.session.query(DBBook).all()
        return results

    # UPDATE BOOK
    def update(self, book: Books):
        db_book = self.get(vo_value(book.book_id))
        if not db_book:
            raise ValueError(f"Book with id {vo_value(book.book_id)} not found")

        db_book.title = vo_value(book.title)
        db_book.author = vo_value(book.author)
        db_book.updated_at = datetime.utcnow()

        self.session.commit()
        self.session.refresh(db_book)
        return db_book


    # DELETE BOOK
    def delete(self, book_id: int):
        db_book = self.get(book_id)
        if not db_book:
            raise ValueError(f"Book with id {book_id} not found")
        self.session.delete(db_book)
        self.session.commit()
        return True

    # BORROW BOOK
    def borrow(self, book_id: int, member_id: int):
        db_book = self.get(book_id)
        if not db_book:
            raise ValueError(f"Book with id {book_id} not found")
        if db_book.is_borrowed:
            raise ValueError(f"Book {db_book.title} is already borrowed")

        db_book.is_borrowed = True
        db_book.borrowed_by = member_id
        db_book.borrowed_date = datetime.utcnow()
        db_book.updated_at = datetime.utcnow()

        self.session.commit()
        self.session.refresh(db_book)
        return db_book

    # RETURN BOOK
    def return_book(self, book_id: int):
        db_book = self.get(book_id)
        if not db_book:
            raise ValueError(f"Book with id {book_id} not found")
        if not db_book.is_borrowed:
            raise ValueError(f"Book {db_book.title} is not borrowed")

        db_book.is_borrowed = False
        db_book.borrowed_by = None
        db_book.borrowed_date = None
        db_book.updated_at = datetime.utcnow()

        self.session.commit()
        self.session.refresh(db_book)
        return db_book
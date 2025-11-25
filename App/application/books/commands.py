# application/books/commands.py
from domain.books.entities import Books
from infrastracture.database.MemberSqlRepository import MemberSQLRepository
from presentation.BookSchema import BookUpdate
from datetime import datetime

class LibraryCommands:
    def __init__(self, repo):
        self.repo = repo  # inject BookSQLRepository

    def add(self, book_data):
        book = Books(
            title=book_data.title,
            author=book_data.author,
            is_borrowed=False,
            borrowed_date=None,
            borrowed_by=None,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        return self.repo.add(book)

    def get(self, book_id: int):
        book = self.repo.get(book_id)
        if not book:
            raise ValueError(f"Book {book_id} not found")
        return book

    def list(self):
        return self.repo.list()

    def update(self, book_id: int, book_data: BookUpdate):
        book = self.repo.get(book_id)
        if not book:
            raise ValueError(f"Book {book_id} not found")
        if not book_data.title:
            raise ValueError("Title is required")
        if not book_data.author:
            raise ValueError("Author is required")
        book.title = book_data.title
        book.author = book_data.author

        return self.repo.update(book)


    def delete(self, book_id: int):
        return self.repo.delete(book_id)

    def borrow(self, book_id: int, member_id: int = None):
        book = self.get(book_id)
        if book.is_borrowed:
            raise ValueError(f"Book '{book.title}' is already borrowed")
        if member_id is None:
            raise ValueError("Member ID is required")
        
        arr = MemberSQLRepository()

        member = arr.get(member_id)
        if member is None:
            raise ValueError(f"Member {member_id} not found")
        book.is_borrowed = True
        book.borrowed_by = member_id
        book.borrowed_date = datetime.utcnow()
        book.updated_at = datetime.utcnow()
        return self.repo.update(book)

    def return_book(self, book_id: int):
        book = self.get(book_id)
        if not book.is_borrowed:
            raise ValueError(f"Book '{book.title}' is not borrowed")
        book.is_borrowed = False
        book.borrowed_by = None
        book.borrowed_date = None
        book.updated_at = datetime.now()
        updated = self.repo.update(book)
        return updated   

from datetime import datetime as dat
from .value_objects import BookId, Title, Author, IsBorrowed, BorrowedDate, BorrowedBy, CreatedAt, UpdatedAt
class Books:
    def __init__(self, title: str, author: str, is_borrowed: bool, borrowed_date: dat, borrowed_by: int, created_at: dat, updated_at: dat):

        self.title = Title(title)
        self.author = Author(author)
        self.is_borrowed = IsBorrowed(is_borrowed)
        self.borrowed_date = BorrowedDate(borrowed_date)
        self.borrowed_by = BorrowedBy(borrowed_by)
        self.created_at = CreatedAt(created_at)
        self.updated_at = UpdatedAt(updated_at)
        
    def borrow(self):
        if self.is_borrowed:
            raise ValueError(f"Book {self.title} is already borrowed")
        self.is_borrowed = True

    def return_book(self):
        if not self.is_borrowed:
            raise ValueError(f"Book {self.title} is not borrowed")
        self.is_borrowed = False

    def update(self, title: str, author: str):
        self.title = title
        self.author = author
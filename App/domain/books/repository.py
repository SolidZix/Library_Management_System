# application/books/repository.py
from abc import ABC, abstractmethod
from ...domain.books.entities import Books
from ...infrastracture.database.database import Session
from ...infrastracture.database.database_models import Books as DBBook
from datetime import datetime
class BookRepository(ABC):
    @abstractmethod
    def add(self, book: Books):
        pass

    @abstractmethod
    def get(self, book_id: int):
        pass

    @abstractmethod
    def list(self):
        pass

    @abstractmethod
    def update(self, book: Books):
        pass

    @abstractmethod
    def delete(self, book_id: int):
        pass

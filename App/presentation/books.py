# presentation/books.py
from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
from typing import List
from ..application.books.commands import BookServices
from infrastracture.database.BookSqlRepository import BookSQLRepository
from presentation.BookSchema import BookCreate, BookResponse, BookUpdate
from uuid import UUID
repo = BookSQLRepository()
commands = BookServices(repo)

router = APIRouter() 


@router.post("/books", response_model=BookResponse)
def add_book(book: BookCreate):    
    try:
        return commands.add(book)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/books", response_model=List[BookResponse])
def list_books():
    return commands.list()


@router.get("/books/{book_id}", response_model=BookResponse)
def get_book_By_Id(book_id: int):
    try:
        return commands.get(book_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, book: BookUpdate):
    try:
        updated_book = commands.update(book_id, book)
        return updated_book
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))



@router.delete("/books/{book_id}")
def delete_book(book_id: int):
    try:
        commands.delete(book_id)
        return {"details:": f"Book {book_id} deleted successfully!"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/books/{book_id}/borrow", response_model=BookResponse)
def borrow_book(book_id: int, member_id: UUID = None):
    try:
        return commands.borrow(book_id, member_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/books/{book_id}/return", response_model=BookResponse)
def return_book(book_id: int):
    try:
        return commands.return_book(book_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

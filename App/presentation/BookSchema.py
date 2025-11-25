from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class BookCreate(BaseModel):
    title: str
    author: str

class BookUpdate(BaseModel):
    title: str 
    author: str

class BookResponse(BaseModel):
    book_id: int
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: Optional[datetime]
    borrowed_by: Optional[UUID]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
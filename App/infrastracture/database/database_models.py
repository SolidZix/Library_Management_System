from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.declarative import declarative_base
import datetime
import uuid

Base = declarative_base()

class Books(Base):
    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    is_borrowed = Column(Boolean, default=False)
    borrowed_date = Column(DateTime, nullable=True)
    borrowed_by = Column(PG_UUID(as_uuid=True), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


class Member(Base):
    __tablename__ = 'members'

    member_id = Column(PG_UUID(as_uuid=True), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

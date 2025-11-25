
from datetime import datetime

class BookId:
    def __init__(self, value: int ):
        if isinstance(value, int):
            self._value = value
        else:
            raise ValueError("book_id must be an integer")

    @property      # to keep the internal value private, prevent accidental modification
    def value(self) -> int:
        return self._value

    def __str__(self):
        return str(self._value)



# Title VO
class Title:
    def __init__(self, value: str):
        value = value.strip()
        if not value:
            raise ValueError("title cannot be empty")
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return self._value


# Author VO
class Author:
    def __init__(self, value: str):
        value = value.strip()
        if not value:
            raise ValueError("author cannot be empty")
        self._value = value

    @property
    def value(self):
        return self._value

    def __str__(self):
        return self._value


# IsBorrowed VO
class IsBorrowed:
    def __init__(self, value: bool = False):
        if not isinstance(value, bool):
            raise ValueError("is_borrowed must be True or False")
        self._value = value

    @property
    def value(self):
        return self._value


# BorrowedDate VO
class BorrowedDate:
    def __init__(self, value: datetime | None = None):
        if value is not None and not isinstance(value, datetime):
            raise ValueError("borrowed_date must be a datetime object or None")
        self._value = value

    @property
    def value(self):
        return self._value

class BorrowedBy:
    def __init__(self, value: int):
        self._value = value

    @property
    def value(self):
        return self._value

# CreatedAt VO
class CreatedAt:
    def __init__(self, value: datetime | None = None):
        self._value = value or datetime.now()

    @property
    def value(self):
        return self._value


# UpdatedAt VO
class UpdatedAt:
    def __init__(self, value: datetime | None = None):
        self._value = value or datetime.now()

    @property
    def value(self):
        return self._value

    def update(self):
        self._value = datetime.now()

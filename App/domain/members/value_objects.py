import uuid
import re
from typing import Optional

class MemberId:
    def __init__(self, value):
        if isinstance(value, str):                 #is value a string?
            try:
                self._value = uuid.UUID(value)     #convert to uuid
            except ValueError:
                raise ValueError("member_id must be a valid UUID string")
        elif isinstance(value, uuid.UUID):
            self._value = value
        else:
            raise ValueError("member_id must be a UUID or string")
        
    @property
    def value(self):
        return self._value
    

class Name:
    def __init__(self, value: str):
        value = value.strip()
        if not value:
            raise ValueError("name cannot be empty")
        self._value = value

    @property
    def value(self):
        return self._value
    def __str__(self):
        return self._value
    

class Email:
    def __init__(self, value: Optional[str]):
        if not value:  # handles None or empty string
            raise ValueError("Email cannot be empty")
        value = value.strip()
        if not self._is_valid_email(value):
            raise ValueError("email must be a valid email address")
        self._value = value
    
    @staticmethod
    def _is_valid_email(value: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, value) is not None
    
    @property
    def value(self) -> Optional[str]:
        return self._value

    def __str__(self) -> str:
        return self._value or ""
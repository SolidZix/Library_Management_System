from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

# Request model for creating/updating a member
class MemberCreate(BaseModel):
    name: str
    email: str

# Response model for returning member info
class MemberResponse(BaseModel):
    member_id: UUID
    name: str
    email: str
    class Config:
        orm_mode = True  # allows Pydantic to read attributes from SQLAlchemy models

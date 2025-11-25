from abc import ABC, abstractmethod
from uuid import UUID
from domain.members.entities import Member
from infrastracture.database.database import Session
from infrastracture.database.database_models import Member as DBMember

class MemberRepository(ABC):
    @abstractmethod
    def add(self, member: Member):
        pass

    @abstractmethod
    def get(self, member_id: UUID) -> Member:
        pass

    @abstractmethod
    def list(self) -> list[Member]:
        pass

    @abstractmethod
    def update(self, member: Member):
        pass

    @abstractmethod
    def delete(self, member_id: UUID):    
        pass
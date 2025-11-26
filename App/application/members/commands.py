from domain.members.entities import Member
from uuid import UUID


class MemberServices:
    def __init__(self, member_repo, book_repo):
        self.member_repo = member_repo
        self.book_repo = book_repo

    def add(self, member: Member):
        db_member = self.member_repo.add(member)
        return db_member

    def get(self, member_id: UUID):
        return self.member_repo.get(member_id)

    def update(self, member: Member):
        return self.member_repo.update(member)


    def delete(self, member_id: UUID):  
        self.member_repo.delete(member_id)

    def list(self):
        return self.member_repo.list()

    # BORROW / RETURN
    def borrow_book(self, book_id: int, member_id: UUID):
        book = self.book_repo.get(book_id)
        member = self.member_repo.get(member_id)

        if book is None:
            raise ValueError(f"Book {book_id} not found")
        if member is None:
            raise ValueError(f"Member {member_id} not found")
        
        member.borrow_book(book)  # domain rules
        book.borrow()
        self.book_repo.update(book)
        self.member_repo.update(member)

    def return_book(self, book_id: int, member_id: UUID):
        book = self.book_repo.get(book_id)
        member = self.member_repo.get(member_id)

        if book is None:
            raise ValueError(f"Book {book_id} not found")
        if member is None:
            raise ValueError(f"Member {member_id} not found")   
             
        member.return_book(book)  # domain rules
        book.return_book() 
        self.book_repo.update(book)
        self.member_repo.update(member)
from ...domain.members.entities import Member
from ...domain.members.value_objects import MemberId, Name, Email
from ...infrastracture.database.database import Session
from ...infrastracture.database.database_models import Member as DBMember
from datetime import datetime
from ...domain.members.repository import MemberRepository
from uuid import UUID
import uuid
from uuid import uuid4


class MemberSQLRepository(MemberRepository):
    def __init__(self):
        self.session = Session()

    # ----------------------------
    # ADD MEMBER
    # ----------------------------
    def add(self, member: Member):
        if member.name.value == "" or member.email.value == "": 
            raise ValueError("Name and email are required")
        
        existing = self.session.query(DBMember).filter_by(email=member.email.value).first() #checking if the email is in-use
        if existing:
            raise ValueError(f"Email '{member.email}' is already in use")
        
        db_member = DBMember(
            member_id=member.member_id.value if hasattr(member.member_id, "value") else uuid4(),
            name=member.name.value if hasattr(member.name, "value") else member.name,
            email=member.email.value if hasattr(member.email, "value") else member.email,
        )
        self.session.add(db_member)
        self.session.commit()
        self.session.refresh(db_member)
        return db_member  # ✅ return the DB object
    # ----------------------------
    # GET MEMBER
    # ----------------------------
    def get(self, member_id: UUID) -> Member:
        db_member = self.session.query(DBMember).filter_by(member_id=member_id).first()
        if not db_member:
            return None
        return Member(
            member_id=MemberId(db_member.member_id),
            name=Name(db_member.name),
            email=Email(db_member.email)
        )

    # ----------------------------
    # LIST MEMBERS
    # ----------------------------
    def list(self) -> list[Member]:
        db_members = self.session.query(DBMember).all()
        return [
            Member(
                member_id=MemberId(m.member_id),
                name=Name(m.name),
                email=Email(m.email)
            ) for m in db_members
        ]

    # ----------------------------
    # UPDATE MEMBER
    # ----------------------------
    def update(self, member: Member):
        db_member = self.session.query(DBMember).filter_by(
            member_id=member.member_id.value
        ).first()

        if not db_member:
            raise ValueError(f"Member {member.member_id.value} not found")
        
        existing = self.session.query(DBMember).filter_by(email=member.email.value).first() #checking if the email is in-use
        if existing:
            raise ValueError(f"Email '{member.email}' is already in use")

        db_member.name = member.name.value
        db_member.email = member.email.value
        db_member.updated_at = datetime.utcnow()

        self.session.commit()
        self.session.refresh(db_member)

        # Return domain Member instead of DB object
        return Member(
            member_id=MemberId(db_member.member_id),
            name=Name(db_member.name),
            email=Email(db_member.email)
        )


    # ----------------------------
    # DELETE MEMBER
    # ----------------------------
    def delete(self, member_id: UUID):
        db_member = self.session.query(DBMember).filter_by(member_id=member_id).first()
        if db_member:
            self.session.delete(db_member)
            self.session.commit()
        return db_member

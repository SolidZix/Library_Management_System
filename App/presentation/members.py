from fastapi import FastAPI, HTTPException, APIRouter
from application.members.commands import MemberServices
from infrastracture.database.MemberSqlRepository import MemberSQLRepository
from domain.members.entities import Member, MemberId, Name, Email
from infrastracture.database.BookSqlRepository import BookSQLRepository
from presentation.MemberSchema import MemberCreate, MemberResponse
from presentation.mapper import member_to_schema
from uuid import UUID
from uuid import uuid4
from typing import List

member_repo = MemberSQLRepository()
book_repo = BookSQLRepository()
commands = MemberServices(member_repo, book_repo)

router = APIRouter()  


@router.post("/members", response_model=MemberResponse)
def add_member(member_create: MemberCreate):
        try:
            member = Member(
                member_id=MemberId(uuid4()),      # auto-generate ID
                name=Name(member_create.name),
                email=Email(member_create.email)
            )

            db_member = commands.add(member)

            return MemberResponse(
                member_id=db_member.member_id,
                name=db_member.name,
                email=db_member.email
            )

        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))


@router.get("/members", response_model=List[MemberResponse])
def list_members():
    members = commands.list()  
    return [member_to_schema(m) for m in members]

@router.get("/members/{member_id}", response_model=MemberResponse)
def get_member_By_Id(member_id: UUID):
    member = commands.get(member_id)
    
    if not member:
        raise HTTPException(status_code=404, detail=f"Member {member_id} not found")

    return member_to_schema(member)

@router.put("/members/{member_id}", response_model=MemberResponse)
def update_member(member_id: UUID, member_data: MemberCreate):
    try:
        member = Member(
            member_id=MemberId(member_id),
            name=Name(member_data.name),
            email=Email(member_data.email)
        )

        updated_member = commands.update(member)  
        return member_to_schema(updated_member)   
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


    
@router.delete("/members/{member_id}")
def delete_member(member_id: UUID):
    if not commands.get(member_id):
        raise HTTPException(status_code=404, detail=f"Member {member_id} not found")
    try:
        commands.delete(member_id)
        return {"detail": f"Member {member_id} deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
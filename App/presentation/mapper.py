# presentation/members/mappers.py
from domain.members.entities import Member
from presentation.MemberSchema import MemberResponse

def member_to_schema(member: Member) -> MemberResponse:
    return MemberResponse(
        member_id=member.member_id.value,         
        name=str(member.name) if hasattr(member.name, "value") else member.name,
        email=str(member.email) if member.email and hasattr(member.email, "value") else member.email
    )
from .value_objects import MemberId, Name, Email

class Member:
    def __init__(self, member_id: MemberId, name: Name, email: Email):
        self.member_id = member_id
        self.name = name
        self.email = email

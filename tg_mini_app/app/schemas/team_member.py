from pydantic import BaseModel

class AddMember(BaseModel):
    user_id: int
    is_captain: bool = False

from pydantic import BaseModel
from typing import Optional, List
from .user import UserOut

class TeamCreate(BaseModel):
    name: str

class TeamOut(BaseModel):
    id: int
    name: str
    members: List[UserOut] = []

    class Config:
        orm_mode = True

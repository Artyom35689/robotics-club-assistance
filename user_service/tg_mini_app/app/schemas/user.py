from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    telegram_id: int
    username: Optional[str]
    full_name: Optional[str]

class UserOut(BaseModel):
    id: int
    telegram_id: int
    username: Optional[str]
    full_name: Optional[str]
    level: int
    xp: int
    is_admin: bool

    class Config:
        orm_mode = True

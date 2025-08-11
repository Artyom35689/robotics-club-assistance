from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime, func
from app.core.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String)
    full_name = Column(String)
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())

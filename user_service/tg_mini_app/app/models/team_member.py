from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, UniqueConstraint, func
from app.core.db import Base

class TeamMember(Base):
    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    team_id = Column(Integer, ForeignKey("teams.id", ondelete="CASCADE"), nullable=False)
    is_captain = Column(Boolean, default=False)
    joined_at = Column(DateTime, default=func.now())

    __table_args__ = (UniqueConstraint('user_id', 'team_id', name='uix_user_team'),)

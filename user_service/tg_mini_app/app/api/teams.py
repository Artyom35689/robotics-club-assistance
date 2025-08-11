from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from app.core.db import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.team.TeamOut)
def create_team(team: schemas.team.TeamCreate, db: Session = Depends(get_db)):
    db_team = models.team.Team(name=team.name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

@router.post("/{team_id}/add", response_model=schemas.team.TeamOut)
def add_user_to_team(team_id: int, member: schemas.team_member.AddMember, db: Session = Depends(get_db)):
    db_team = db.query(models.team.Team).filter(models.team.Team.id == team_id).first()
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    
    # Проверка: не в команде ли уже
    existing = db.query(models.team_member.TeamMember).filter_by(user_id=member.user_id, team_id=team_id).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already in team")

    new_member = models.team_member.TeamMember(
        user_id=member.user_id,
        team_id=team_id,
        is_captain=member.is_captain
    )
    db.add(new_member)
    db.commit()
    return get_team_info(team_id, db)

@router.get("/{team_id}", response_model=schemas.team.TeamOut)
def get_team_info(team_id: int, db: Session = Depends(get_db)):
    team = (
        db.query(models.team.Team)
        .options(joinedload(models.team.Team.members))
        .filter(models.team.Team.id == team_id)
        .first()
    )
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")

    # Загружаем участников
    member_ids = db.query(models.team_member.TeamMember.user_id).filter_by(team_id=team.id).all()
    user_ids = [uid for (uid,) in member_ids]
    users = db.query(models.user.User).filter(models.user.User.id.in_(user_ids)).all()
    
    return schemas.team.TeamOut(
        id=team.id,
        name=team.name,
        members=users
    )

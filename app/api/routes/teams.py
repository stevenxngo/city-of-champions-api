from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...dependencies import get_db
from ..models import Team   
from ..schemas import TeamSchema
from typing import List

router = APIRouter()


@router.get("/", response_model=List[TeamSchema])
def get_teams(db: Session = Depends(get_db)):
    return db.query(Team).all()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...dependencies import get_db
from ..models import League
from ..schemas import LeagueSchema
from typing import List

router = APIRouter()


@router.get("/", response_model=List[LeagueSchema])
def get_leagues(db: Session = Depends(get_db)):
    return db.query(League).all()

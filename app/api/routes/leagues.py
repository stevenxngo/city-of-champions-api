from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ...dependencies import get_db
from ..models import League
from ..schemas import LeagueSchema
from ...crud.leagues_crud import *

router = APIRouter()


@router.get("/", response_model=List[LeagueSchema])
def fetch_leagues(db: Session = Depends(get_db)):
    return db.query(League).all()


@router.get("/id/{league_id}", response_model=LeagueSchema)
def fetch_league_by_id(
    league_id: int = Path(..., title="League ID"),
    db: Session = Depends(get_db),
):
    league = get_league_by_id(db, league_id)
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    return league


@router.get("/name/{league_name}", response_model=LeagueSchema)
def fetch_league_by_name(
    league_name: str = Path(..., title="League Name"),
    db: Session = Depends(get_db),
):
    league = get_league_by_name(db, league_name)
    if not league:
        raise HTTPException(status_code=404, detail="League not found")
    return league

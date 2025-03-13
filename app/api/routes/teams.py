from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from typing import List
from ...dependencies import get_db
from ..schemas import TeamSchema
from ...crud.teams_crud import *

router = APIRouter()


@router.get("/", response_model=List[TeamSchema])
def fetch_teams(db: Session = Depends(get_db)):
    return get_teams(db)


@router.get("/id/{team_id}", response_model=TeamSchema)
def fetch_team_by_id(
    team_id: int = Path(..., title="Team ID"), db: Session = Depends(get_db)
):
    team = get_team_by_id(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.get("/name/{team_name}", response_model=TeamSchema)
def fetch_team_by_name(
    team_name: str = Path(..., title="Team Name"), db: Session = Depends(get_db)
):
    team = get_team_by_name(db, team_name)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

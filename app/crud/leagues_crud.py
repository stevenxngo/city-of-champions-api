from sqlalchemy import func
from sqlalchemy.orm import Session
from ..api.models import League


def get_all_leagues(db: Session):
    return db.query(League).all()


def get_league_by_id(db: Session, league_id: str):
    return db.query(League).filter(League.id == league_id).first()


def get_league_by_name(db: Session, league_name: str):
    return (
        db.query(League)
        .filter(func.lower(League.name) == league_name.lower())
        .first()
    )

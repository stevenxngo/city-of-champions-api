from sqlalchemy import func
from sqlalchemy.orm import Session
from ..api.models import City


def get_cities(db: Session):
    return db.query(City).all()


def get_city_by_id(db: Session, city_id: int):
    return db.query(City).filter(City.id == city_id).first()


def get_city_by_name(db: Session, city_name: str):
    return (
        db.query(City)
        .filter(func.lower(City.name) == city_name.lower())
        .first()
    )

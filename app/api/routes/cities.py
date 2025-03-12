from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import get_db
from api.models import City
from api.schemas import CitySchema
from typing import List

router = APIRouter()


@router.get("/", response_model=List[CitySchema])
def get_cities(db: Session = Depends(get_db)):
    return db.query(City).all()

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from typing import List
from ...dependencies import get_db
from ..models import City
from ..schemas import CitySchema
from ...crud.cities_crud import *

router = APIRouter()


@router.get("/", response_model=List[CitySchema])
def fetch_cities(db: Session = Depends(get_db)):
    return get_cities(db)


@router.get("/id/{city_id}", response_model=CitySchema)
def fetch_city_by_id(
    city_id: int = Path(..., title="City ID"), db: Session = Depends(get_db)
):
    return get_city_by_id(db, city_id)


@router.get("/name/{city_name}", response_model=CitySchema)
def fetch_city_by_name(
    city_name: str = Path(..., title="City Name"), db: Session = Depends(get_db)
):
    return get_city_by_name(db, city_name)

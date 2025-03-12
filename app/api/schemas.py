from pydantic import BaseModel

class CitySchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

class LeagueSchema(BaseModel):
    id: int
    name: str
    sport: str

    class Config:
        orm_mode = True

class TeamSchema(BaseModel):
    id: int
    location: str
    name: str
    city_id: int
    league_id: int
    championships: int
    appearances: int

    class Config:
        orm_mode = True

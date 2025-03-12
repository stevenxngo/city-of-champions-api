from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..data.database import Base

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    teams = relationship("Team", back_populates="city")

class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    sport = Column(String, nullable=False)

    teams = relationship("Team", back_populates="league")

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)
    name = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"), nullable=False)
    league_id = Column(Integer, ForeignKey("leagues.id"), nullable=False)
    championships = Column(Integer, default=0)
    appearances = Column(Integer, default=0)

    city = relationship("City", back_populates="teams")
    league = relationship("League", back_populates="teams")

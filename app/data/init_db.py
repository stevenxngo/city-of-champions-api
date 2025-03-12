from data.database import engine, Base
from api.models import City, League, Team
import pandas as pd
from sqlalchemy.orm import Session
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

Base.metadata.create_all(bind=engine)


def import_csv():
    db = Session(bind=engine)

    leagues_df = pd.read_csv(BASE_DIR / "leagues.csv")
    for _, row in leagues_df.iterrows():
        db.add(League(id=row["id"], name=row["name"], sport=row["sport"]))

    teams_df = pd.read_csv(BASE_DIR / "teams.csv")
    unique_cities = teams_df["city"].unique()
    for city in unique_cities:
        db.add(City(name=city))

    db.commit()

    for _, row in teams_df.iterrows():
        city = db.query(City).filter_by(name=row["city"]).first()
        league = db.query(League).filter_by(name=row["league"]).first()

        db.add(
            Team(
                id=row["id"],
                location=row["location"],
                name=row["team"],
                city_id=city.id,
                league_id=league.id,
                championships=row["championships"],
                appearances=row["appearances"],
            )
        )

    db.commit()
    db.close()


import_csv()

from sqlalchemy import func
from sqlalchemy.orm import Session
from ..api.models import Team


def get_teams(db: Session):
    return db.query(Team).all()


def get_team_by_id(db: Session, team_id: int):
    return db.query(Team).filter(Team.id == team_id).first()


def get_team_by_name(db: Session, team_name: str):
    locations = [team.location for team in db.query(Team.location).distinct()]
    locations.sort(key=len, reverse=True)

    team_name_lower = team_name.lower()

    for location in locations:
        location_lower = location.lower()

        if team_name_lower.startswith(location_lower):
            team_name_part = team_name[len(location) :].strip()
            return (
                db.query(Team)
                .filter(
                    func.lower(Team.location) == location_lower,
                    func.lower(Team.name) == team_name_part.lower(),
                )
                .first()
            )

    return None

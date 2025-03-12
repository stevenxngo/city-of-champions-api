from fastapi import FastAPI
from api.routes import cities, teams, leagues

app = FastAPI(title="City of Champions")

app.include_router(cities.router, prefix="/city", tags=["Cities"])
app.include_router(teams.router, prefix="/team", tags=["Teams"])
app.include_router(leagues.router, prefix="/league", tags=["Leagues"])


@app.get("/")
def root():
    return {"message": "City of Champions API"}

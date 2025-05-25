from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models
from .database import core
from .database import schemas

# Instantiate the web application
app = FastAPI()

# Connect to database: Creates engine and Sessions constructor.
db = core.DataBase("sqlite+pysqlite:///../database/test.db")

# Endpoints operations
# 1) /move endpoint
@app.post("/move", status_code=200)
async def move(
    move : models.MoveModel
):
    return move

# 2) /status
@app.get("/status", status_code=200)
def status(
    matchId : int,
    session : Session = Depends(db.get_session)
):
    match = session.query(schemas.MatchSchema).filter(schemas.MatchSchema.id == matchId).first()
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    print(match)
    return models.MatchModel(id=1)

# 3) /create
@app.post("/create", status_code=200)
async def create():
    match = models.MatchModel(id=1)
    return match.id
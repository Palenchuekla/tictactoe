import os

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import models
from . import crud_operations
from .database import core
from .database import schemas

# Check that the BD URL exists
if not "DB_URL" in os.environ:
    raise Exception(f"Database URL( \"DB_URL\" environment variable) not defined!")

# Connect to database: creates engine and session generator
db = core.DataBase(f"{os.environ["DB_URL"]}")

# Instantiate the web application
app = FastAPI()

# Endpoints operations
# 1) /move
@app.post("/move", status_code=200)
async def move(
    move : models.MoveModel,
    session : Session = Depends(db.get_session_to_db_FastAPI)
):
    move_db, match_db = crud_operations.post_move(move=move, session=session)
    return {"posted_move":move_db, "match":match_db}

# 2) /status
@app.get("/status", status_code=200)
def status(
    matchId : int,
    session : Session = Depends(db.get_session_to_db_FastAPI)
):
    db_match = crud_operations.get_match_by_id(matchId, session)
    if not db_match:
        raise HTTPException(status_code=404, detail="Match not found")
    return db_match

# 3) /create
@app.post("/create", status_code=200)
async def create(
    match   : models.MatchModel | None = None,
    session : Session = Depends(db.get_session_to_db_FastAPI)
):
    if match == None:
        match = models.MatchModel()
    db_match = crud_operations.post_match_by_id(match=match, session=session)
    return {"idMatch":db_match.id}
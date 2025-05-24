# Import the FastAPI module
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Any

# Instantiate the web application
app = FastAPI()

# Endpoints operations

# 1) /move endoint
class Square(BaseModel):
    x : int = Field(ge=0, le=2)
    y : int = Field(ge=0, le=2)

class Move(BaseModel):
    matchId : int
    playerId : str
    # Literal["created_at", "updated_at"] = "created_at"
    square: Square

@app.post("/move", status_code=200)
async def move(
    move : Move
):
    return move

# 2) /status
class Match(BaseModel):
    id : int

@app.get("/status", status_code=200, response_model=Match)
async def status(
    matchId : int
):
    match = Match(id=matchId)
    return match

# 3) /create
@app.post("/create", status_code=200)
async def create():
    match = Match(id=1)
    return match.id
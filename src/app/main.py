# Import the FastAPI module
from fastapi import FastAPI
from models.models import Match, Move

# Instantiate the web application
app = FastAPI()

# Endpoints operations

# 1) /move endoint
@app.post("/move", status_code=200)
async def move(
    move : Move
):
    return move

# 2) /status
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
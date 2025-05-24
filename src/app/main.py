# Import the FastAPI module
from fastapi import FastAPI
from pydantic import BaseModel, Field

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
    square: Square

@app.post("/move", status_code=200)
async def move(
    move : Move
):
    return move
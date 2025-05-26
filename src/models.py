from pydantic import BaseModel, Field

class SquareModel(BaseModel):
    x : int = Field(ge=1, le=3)
    y : int = Field(ge=1, le=3)
    
class MoveModel(BaseModel):
    matchId : int
    playerId : str = Field(pattern="^(X|O)$")
    square: SquareModel

class MatchModel(BaseModel):
    id: int | None = None
    turn : str = Field(pattern="^(X|O)$", default="X")
    winner : str | None = Field(pattern="^(X|O)$", default=None)
    board : str = Field(pattern="^[XO_]{9}$", default="_________")
from pydantic import BaseModel, Field

class SquareModel(BaseModel):
    x : int = Field(ge=0, le=2)
    y : int = Field(ge=0, le=2)
    
class MoveModel(BaseModel):
    matchId : int
    playerId : str
    # Literal["created_at", "updated_at"] = "created_at"
    square: SquareModel

class MatchModel(BaseModel):
    id: int | None = None
    turn : str = Field(pattern="^(X|O|_)$")
    board : str = Field(pattern="^[XO_]{9}$")
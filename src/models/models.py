from pydantic import BaseModel, Field

class Square(BaseModel):
    x : int = Field(ge=0, le=2)
    y : int = Field(ge=0, le=2)
    
class Move(BaseModel):
    matchId : int
    playerId : str
    # Literal["created_at", "updated_at"] = "created_at"
    square: Square

class Match(BaseModel):
    id : int

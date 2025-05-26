from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, CHAR, ForeignKey, Boolean

Base = declarative_base()

class MatchSchema(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    turn = Column(CHAR(1), nullable=False)
    winner = Column(CHAR(1), nullable=True, default=None)
    board = Column(CHAR(9), nullable=False, default="_________")

    def __repr__(self):
        r = f"<Match(id={self.id}, turn={self.turn}, board={self.board})>"
        r+=f"\t\t\n{self.board[0:3]}"
        r+=f"\t\t\n{self.board[3:6]}"
        r+=f"\t\t\n{self.board[6:9]}"
        r+=f"\n\n"
        return r
    
class MoveSchema(Base):
    __tablename__ = "moves"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    matchId = Column(Integer, ForeignKey('matches.id'), index=True)
    playerId = Column(CHAR(1), nullable=False)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)
    
    def __repr__(self):
        r = f"<Move(id={self.id}, matchId={self.matchId}, playerId={self.playerId}), x={self.x}, y={self.y}>"
        return r
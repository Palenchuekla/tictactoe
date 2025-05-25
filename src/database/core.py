from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .schemas import Base, MatchSchema

class DataBase():
    def __init__(self, url : str):
        self.url        = url
        self.engine     = create_engine(self.url, connect_args={"check_same_thread": False})
        self.Session    = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    
    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)
    
    def get_session(self):
        session = self.Session()
        try:
            yield session
        finally:
            session.close()
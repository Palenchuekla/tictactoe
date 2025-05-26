from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .schemas import Base

class DataBase():
    def __init__(self, url : str):
        self.url            = url
        self.engine         = create_engine(self.url, connect_args={"check_same_thread": False})
        self.session_maker  = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)

    @contextmanager
    def get_session_to_db_NOFastAPI(self):
        ''''
        Returns a session to self.database that closes automatically.
        Usefull when NOT using FastAPI.
        '''
        db = self.session_maker()
        try:
            yield db
        finally:
            db.close()
    
    def get_session_to_db_FastAPI(self):
        '''
        Returns a session to self.database that closes automatically.
        Usefull when using FastAPI.
        '''
        db = self.session_maker()
        try:
            yield db
        finally:
            db.close()
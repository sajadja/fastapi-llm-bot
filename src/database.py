import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./db/app_data.sqlite"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    '''
    returns a db session.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    '''
    create db folder and create tables in database
    '''
    os.makedirs("db", exist_ok=True)
    Base.metadata.create_all(bind=engine)

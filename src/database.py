from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///./SQLite.db"

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
    initialize database and create tables
    '''
    Base.metadata.create_all(bind=engine)
    # session = SessionLocal()

    # # insert sample data
    # if not session.query(Product).first():
    #     with open("product/sample_data.json", "r") as f:
    #         data = json.load(f)
    #     objects = [Product(**item) for item in data]
    #     session.add_all(objects)
    #     session.commit()

    # session.close()

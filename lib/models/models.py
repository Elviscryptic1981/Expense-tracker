from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import SessionLocal

DATABASE_URL = "sqlite:///./finance.db"

engine = create_engine(DATABASE_URL)
SessionLocal = SessionLocal(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

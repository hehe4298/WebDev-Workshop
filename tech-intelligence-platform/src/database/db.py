from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base

# Using SQLite for version 1
DATABASE_URL = "sqlite:///tech_intelligence.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Create all tables in the database."""
    Base.metadata.create_all(bind=engine)

def get_session():
    """Get a database session."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

def get_session_context():
    """Helper for using session as context manager manually if needed."""
    return SessionLocal()

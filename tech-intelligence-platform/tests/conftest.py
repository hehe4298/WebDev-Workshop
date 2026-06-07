import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import contextlib

from src.models.models import Base
from src.database.db import get_session_context

@pytest.fixture(scope="session")
def test_engine():
    # Use an in-memory SQLite database for testing
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(bind=engine)
    return engine

@pytest.fixture(scope="function")
def test_session(test_engine):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.rollback()
        # Clean up tables after each test to ensure isolation
        for table in reversed(Base.metadata.sorted_tables):
            session.execute(table.delete())
        session.commit()
        session.close()

@pytest.fixture(autouse=True)
def override_get_session_context(monkeypatch, test_session):
    """
    Override the database connection to use the test session everywhere.
    """
    @contextlib.contextmanager
    def mock_get_session_context():
        yield test_session

    monkeypatch.setattr("src.collectors.rss_collector.get_session_context", mock_get_session_context)
    monkeypatch.setattr("src.reporting.generator.get_session_context", mock_get_session_context)

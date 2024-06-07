import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.main import app
from app.database import Base
from app.models import Feedback

SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://aditya:admin@localhost/test_feedback"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

client = TestClient(app)

@pytest.fixture(scope="module")
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_create_feedback(db):
    response = client.post("/feedback/", json={"score": 5})
    assert response.status_code == 200
    assert response.json()["score"] == 5

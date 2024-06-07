# test_feedback.py

import os
from dotenv import load_dotenv
import pytest # type: ignore
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.models import Base, Feedback
import asyncio

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DB_USER = os.getenv("USER")
DB_PASSWORD =os.getenv("PASSWORD")
DB_NAME = os.getenv("DATABASENAME")
DB_HOST = os.getenv("HOST")
DB_PORT = 5432

SQLALCHEMY_DATABASE_URL = DATABASE_URL

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

@pytest.fixture(scope="module", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

@pytest.fixture(scope="function")
async def db_session():
    async with TestingSessionLocal() as session:
        yield session

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

@pytest.mark.asyncio
async def test_create_feedback(client):
    response = client.post("/feedback/", json={"rating": 5})
    assert response.status_code == 200
    assert response.json()["rating"] == 5

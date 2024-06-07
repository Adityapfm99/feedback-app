
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
DB_USER = os.getenv("USER")
DB_PASSWORD =os.getenv("PASSWORD")
DB_NAME = os.getenv("DATABASENAME")
DB_HOST = os.getenv("HOST")
DB_PORT = 5432

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{(DB_PORT)}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

async def get_db():
    async with SessionLocal() as session:
        yield session


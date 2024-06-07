from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Feedback
import uvicorn

DATABASE_URL = "postgresql+asyncpg://aditya:admin@localhost/feedback"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

app = FastAPI()

class FeedbackCreate(BaseModel):
    rating: int

@app.post("/feedback/")
async def create_feedback(feedback: FeedbackCreate):
    async with async_session() as session:
        async with session.begin():
            new_feedback = Feedback(rating=feedback.rating)
            session.add(new_feedback)
        await session.commit()
        return new_feedback

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

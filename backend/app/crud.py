from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from .models import Feedback
from .schemas import FeedbackCreate

async def create_feedback(db: AsyncSession, feedback: FeedbackCreate):
    try:
        db_feedback = Feedback(rating=feedback.rating)
        db.add(db_feedback)
        await db.commit()
        await db.refresh(db_feedback)
        return {"rating": db_feedback.rating} 
    except SQLAlchemyError as e:
        await db.rollback()
        raise e

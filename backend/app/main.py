import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, conint, validator
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from app.models import Base, Feedback
import uvicorn

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

#custom error message
class CustomHTTPException(HTTPException): 
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail
        self.state = 'error'

# init swagger

app = FastAPI(
    title="App Feedback API",
    description="API for collecting feedback about the application",
    version="1.0.0",

    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
class FeedbackCreate(BaseModel):
    rating: int

    @validator('rating')
    def rating_must_be_between_1_and_5(cls, rat):
        if rat is None or rat < 1 or rat > 5:
            raise CustomHTTPException(status_code=400, detail='Rating must be between 1 and 5')
        return rat

@app.exception_handler(CustomHTTPException)
async def custom_http_exception_handler(request: Request, exc: CustomHTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.status_code,"status": exc.state, "message": exc.detail},
    
    )

@app.post("/feedback/", response_model=dict, summary="Create Feedback", description="Create a new feedback with a rating between 1 and 5")
async def create_feedback(feedback: FeedbackCreate):

    async with async_session() as session:
        async with session.begin():
            query = text("INSERT INTO feedback (rating) VALUES (:rating)")
            await session.execute(query, {"rating": feedback.rating})
        await session.commit()
        return {"status": "success", "rating": feedback.rating}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

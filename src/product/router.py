from fastapi import APIRouter, Depends
from .schemas import UserMessage, BotResponse, ProductsData
from sqlalchemy.orm import Session
from src.database import get_db
from .models import Product
from .rag import RAGSystem
from src.gemini.client import GeminiClient

router = APIRouter(
    prefix="/product",
    tags=["product"]
)


@router.get('/db_data', response_model=ProductsData)
async def db_data(db: Session = Depends(get_db)):
    data = {
        'records_count': db.query(Product).count(),
        'first_10_records': db.query(Product).limit(10)
    }
    return data


@router.post('/simulate_dm', response_model=BotResponse)
async def simulate_dm(user_message: UserMessage):
    gemini = GeminiClient()
    rag = RAGSystem(ai_model=gemini)
    answer = rag.generate_answer(user_message.text)
    return {'reply': answer}

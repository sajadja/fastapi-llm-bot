import json
from src.product.models import Product
from fastapi import FastAPI
from .database import init_db
from contextlib import asynccontextmanager
from .database import SessionLocal
from .product import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()

    # insert sample data
    session = SessionLocal()
    if not session.query(Product).first():
        with open("src/product/sample_data.json", "r") as f:
            data = json.load(f)
        objects = [Product(**item) for item in data]
        session.add_all(objects)
        session.commit()
        session.close()
    yield


app = FastAPI(
    title="Gemini RAG Chatbot",
    description="A chatbot that uses RAG with SQLite and Gemini for product queries",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(product_router.router)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

from fastapi import FastAPI


app = FastAPI(
    title="Gemini RAG Chatbot",
    description="A chatbot that uses RAG with SQLite and Gemini for product queries",
    version="1.0.0"
)


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

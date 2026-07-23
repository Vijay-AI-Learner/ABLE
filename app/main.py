from fastapi import FastAPI

app = FastAPI(
    title="ABLE AI Platform",
    description="Enterprise AI Platform for Generative AI, RAG, and Agentic AI",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to ABLE AI Platform"
    }

@app.get("/health")
def health():
    return {
        "status": "UP"
    }
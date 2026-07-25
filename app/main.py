from fastapi import FastAPI
from app.api.v1.health import router as health_router

app = FastAPI(
    title="ABLE AI Platform",
    version="1.0.0",
    description="Enterprise AI Platform"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to ABLE AI Platform"
    }
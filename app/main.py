from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.v1.users import router as user_router
from app.api.v1.health import router as health_router

from app.core.settings import settings
from app.database.connection import Base, engine

# Import all models here
from app.models.user import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    yield
    print("Application shutting down...")


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Enterprise AI Platform",
    lifespan=lifespan
)

app.include_router(health_router)
app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to ABLE AI Platform"
    }
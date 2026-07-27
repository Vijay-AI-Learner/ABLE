from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.v1.users import router as user_router
from app.api.v1.health import router as health_router
from app.api.v1.auth import router as auth_router
from app.api.v1.me import router as me_router
from app.core.settings import settings
from app.database.connection import Base, engine
from app.api.v1.admin import router as admin_router
from app.exceptions.handlers import generic_exception_handler
# Import all models here
from app.models.user import User
from app.core.logger import logger
from app.middleware.logging import LoggingMiddleware
from app.api.v1.documents import router as document_router

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

logger.info("ABLE Platform Started")
app.include_router(health_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(me_router)
app.include_router(admin_router)
app.add_middleware(LoggingMiddleware)
app.include_router(document_router)
@app.get("/")
def root():
    return {
        "message": "Welcome to ABLE AI Platform"
    }
app.add_exception_handler(
    Exception,
    generic_exception_handler
)
logger.info("ABLE Platform Started")
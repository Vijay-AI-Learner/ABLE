print("Loading connection.py...")
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings
from app.database.base import Base


engine = create_engine(
    settings.database_url,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Import all models BEFORE create_all()
from app.models.user import User

print("Creating tables...")

Base.metadata.create_all(bind=engine)

print("Finished create_all()")
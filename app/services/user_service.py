from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password
from app.repositories.user_repository import user_repository
from app.core.logger import logger


def create_user(db: Session, user: UserCreate):

    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
        role="user"
    )

    return user_repository.create(db, db_user)
    logger.info(
        f"User created: {db_user.username}"
    )
    

def get_user_by_username(db, username: str):

    return user_repository.get_by_username(db, username)
       
    

def get_user_by_email(db, email: str):

   return user_repository.get_by_email(db, email)
    
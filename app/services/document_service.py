import shutil
import uuid
from pathlib import Path

from sqlalchemy.orm import Session

from app.models.document import Document
from app.repositories.document_repository import document_repository

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


def upload_document(
    db: Session,
    file,
    username: str
):

    extension = Path(file.filename).suffix

    stored_filename = f"{uuid.uuid4()}{extension}"

    destination = UPLOAD_DIR / stored_filename

    with destination.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = Document(
        filename=file.filename,
        stored_filename=stored_filename,
        content_type=file.content_type,
        uploaded_by=username
    )

    return document_repository.create(db, document)
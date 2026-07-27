from sqlalchemy.orm import Session

from app.models.document import Document


class DocumentRepository:

    def create(self, db: Session, document: Document):
        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    def get(self, db: Session, document_id: int):
        return (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )


document_repository = DocumentRepository()
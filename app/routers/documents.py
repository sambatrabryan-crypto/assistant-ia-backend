import os
import shutil
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.document import Document
from app.auth.auth import get_current_user

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
def upload_document(cours_id: int, file: UploadFile = File(...), db: Session = Depends(get_db), user=Depends(get_current_user)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    doc = Document(nom_fichier=file.filename, chemin_fichier=file_path, cours_id=cours_id)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc

@router.get("/")
def list_documents(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Document).all()

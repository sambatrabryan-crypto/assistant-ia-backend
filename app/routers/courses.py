from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.cours import Matiere, Cours
from app.auth.auth import get_current_user
from pydantic import BaseModel

router = APIRouter(prefix="/courses", tags=["Cours"])

class MatiereCreate(BaseModel):
    nom: str

class CoursCreate(BaseModel):
    titre: str
    matiere_id: int

@router.get("/matieres")
def get_matieres(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Matiere).filter(Matiere.utilisateur_id == user.id).all()

@router.post("/matieres")
def create_matiere(data: MatiereCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    matiere = Matiere(nom=data.nom, utilisateur_id=user.id)
    db.add(matiere)
    db.commit()
    db.refresh(matiere)
    return matiere

@router.get("/")
def get_cours(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Cours).join(Matiere).filter(Matiere.utilisateur_id == user.id).all()

@router.post("/")
def create_cours(data: CoursCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    cours = Cours(titre=data.titre, matiere_id=data.matiere_id)
    db.add(cours)
    db.commit()
    db.refresh(cours)
    return cours

from pydantic import BaseModel
from typing import Optional, List

class QuestionCreate(BaseModel):
    texte: str
    choix_a: str
    choix_b: str
    choix_c: Optional[str] = None
    choix_d: Optional[str] = None
    bonne_reponse: str

class QuizCreate(BaseModel):
    titre: str
    cours_id: int
    questions: List[QuestionCreate]

class ReponseEtudiant(BaseModel):
    question_id: int
    reponse_choisie: str

class QuizSubmit(BaseModel):
    quiz_id: int
    reponses: List[ReponseEtudiant]

class QuestionOut(BaseModel):
    id: int
    texte: str
    choix_a: str
    choix_b: str
    choix_c: Optional[str]
    choix_d: Optional[str]
    # note : bonne_reponse n'est PAS renvoyée à l'étudiant avant correction

    class Config:
        from_attributes = True

class QuizOut(BaseModel):
    id: int
    titre: str
    cours_id: int
    questions: List[QuestionOut]

    class Config:
        from_attributes = True
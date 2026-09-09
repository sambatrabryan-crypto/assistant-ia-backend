from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.quiz import Quiz, Question, Resultat
from app.schemas.quiz import QuizCreate, QuizOut, QuizSubmit
from app.auth.auth import get_current_user

router = APIRouter(prefix="/quiz", tags=["Quiz"])

@router.post("/", response_model=QuizOut)
def create_quiz(data: QuizCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    quiz = Quiz(titre=data.titre, cours_id=data.cours_id)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)

    for q in data.questions:
        question = Question(
            quiz_id=quiz.id,
            texte=q.texte,
            choix_a=q.choix_a,
            choix_b=q.choix_b,
            choix_c=q.choix_c,
            choix_d=q.choix_d,
            bonne_reponse=q.bonne_reponse.lower()
        )
        db.add(question)
    db.commit()
    db.refresh(quiz)
    return quiz


@router.get("/{quiz_id}", response_model=QuizOut)
def get_quiz(quiz_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    quiz = db.query(Quiz).filter(Quiz.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz introuvable")
    return quiz


@router.get("/")
def list_quiz(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Quiz).all()


@router.post("/submit")
def submit_quiz(data: QuizSubmit, db: Session = Depends(get_db), user=Depends(get_current_user)):
    questions = db.query(Question).filter(Question.quiz_id == data.quiz_id).all()
    if not questions:
        raise HTTPException(status_code=404, detail="Quiz introuvable ou sans questions")

    questions_map = {q.id: q for q in questions}
    bonnes_reponses = 0

    for reponse in data.reponses:
        question = questions_map.get(reponse.question_id)
        if question and reponse.reponse_choisie.lower() == question.bonne_reponse:
            bonnes_reponses += 1

    total = len(questions)
    score = round((bonnes_reponses / total) * total, 2) if total > 0 else 0

    resultat = Resultat(
        quiz_id=data.quiz_id,
        utilisateur_id=user.id,
        score=score,
        total_questions=total
    )
    db.add(resultat)
    db.commit()
    db.refresh(resultat)

    return {
        "score": score,
        "total": total,
        "bonnes_reponses": bonnes_reponses,
        "resultat_id": resultat.id
    }


@router.get("/resultats/mes-resultats")
def mes_resultats(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Resultat).filter(Resultat.utilisateur_id == user.id).all()
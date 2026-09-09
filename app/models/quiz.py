from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Quiz(Base):
    __tablename__ = "quiz"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    cours_id = Column(Integer, ForeignKey("cours.id"))
    date_creation = Column(DateTime, default=datetime.utcnow)

    questions = relationship("Question", back_populates="quiz", cascade="all, delete-orphan")


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quiz.id"))
    texte = Column(String, nullable=False)
    choix_a = Column(String, nullable=False)
    choix_b = Column(String, nullable=False)
    choix_c = Column(String, nullable=True)
    choix_d = Column(String, nullable=True)
    bonne_reponse = Column(String, nullable=False)  # "a", "b", "c" ou "d"

    quiz = relationship("Quiz", back_populates="questions")


class Resultat(Base):
    __tablename__ = "resultat"
    id = Column(Integer, primary_key=True, index=True)
    quiz_id = Column(Integer, ForeignKey("quiz.id"))
    utilisateur_id = Column(Integer, ForeignKey("utilisateur.id"))
    score = Column(Float, nullable=False)  # ex: 8.0 sur 10
    total_questions = Column(Integer, nullable=False)
    date_passage = Column(DateTime, default=datetime.utcnow)
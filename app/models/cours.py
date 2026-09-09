from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Matiere(Base):
    __tablename__ = "matiere"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateur.id"))
    cours = relationship("Cours", back_populates="matiere")

class Cours(Base):
    __tablename__ = "cours"
    id = Column(Integer, primary_key=True, index=True)
    titre = Column(String, nullable=False)
    matiere_id = Column(Integer, ForeignKey("matiere.id"))
    matiere = relationship("Matiere", back_populates="cours")
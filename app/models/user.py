from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Utilisateur(Base):
    __tablename__ = "utilisateur"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    mot_de_passe_hash = Column(String, nullable=False)
    date_creation = Column(DateTime, default=datetime.utcnow)
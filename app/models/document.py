from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from datetime import datetime
from app.database import Base

class Document(Base):
    __tablename__ = "document"
    id = Column(Integer, primary_key=True, index=True)
    nom_fichier = Column(String, nullable=False)
    chemin_fichier = Column(String, nullable=False)
    cours_id = Column(Integer, ForeignKey("cours.id"))
    date_upload = Column(DateTime, default=datetime.utcnow)
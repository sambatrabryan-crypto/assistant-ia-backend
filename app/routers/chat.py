from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth.auth import get_current_user

router = APIRouter(prefix="/chat", tags=["Assistant IA"])

class ChatRequest(BaseModel):
    message: str
    cours_id: int | None = None

@router.post("/")
def chat(request: ChatRequest, user=Depends(get_current_user)):
    # TODO: brancher ici le module IA (RAG + LLM) de la Personne 3
    return {"reponse": f"[Réponse simulée] Vous avez demandé : {request.message}"}

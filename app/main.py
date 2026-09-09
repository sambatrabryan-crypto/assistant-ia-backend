from fastapi import FastAPI
from app.database import Base, engine
from app.routers import auth, courses, documents, chat, quiz

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Assistant IA pour étudiants - API")

app.include_router(auth.router)
app.include_router(courses.router)
app.include_router(documents.router)
app.include_router(chat.router)
app.include_router(quiz.router)

@app.get("/")
def root():
    return {"message": "API Assistant IA - Backend opérationnel"}
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    nom: str
    email: EmailStr
    mot_de_passe: str

class UserLogin(BaseModel):
    email: EmailStr
    mot_de_passe: str

class UserOut(BaseModel):
    id: int
    nom: str
    email: EmailStr

    class Config:
        from_attributes = True
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from auth.jwt_handler import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: LoginRequest):
    if user.username == "opsuser" and user.password == "securepass":
        token = create_access_token({"sub": user.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

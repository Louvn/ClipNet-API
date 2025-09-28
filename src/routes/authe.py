from fastapi import APIRouter, Body, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt, time, os
from ..database import get_db

router = APIRouter(tags=["authentification"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

@router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):
    payload = {"sub": form.username, "exp": int(time.time()) + 3600}
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}

#@router.post("/register")
def register(username: str = Body(...), password: str = Body(...), token: str = Body(...), db = Depends(get_db)):
    return "Hello!"

@router.get("/test")
def test(token: str = Depends(oauth2_scheme)):
    return "Hello"
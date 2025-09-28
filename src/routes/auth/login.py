from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt, time, os
from src.database import get_db
from src.models import User
from src.utils.hash import verify

router = APIRouter(tags=["authentification"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

def login(form: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == form.username).first()
    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    if not verify(form.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    payload = {"sub": form.username, "exp": int(time.time()) + 3600}
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
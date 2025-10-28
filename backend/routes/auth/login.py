from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import jwt, time, os
from backend.database import get_db
from backend.models import User
from backend.utils.hash import verify

SECRET = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("JWT_ALGORITHM")

def login(form: OAuth2PasswordRequestForm = Depends(), db = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == form.username).first()
    if not existing_user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    if not verify(form.password, existing_user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    payload = {"sub": form.username, "exp": int(time.time()) + 3600}
    token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
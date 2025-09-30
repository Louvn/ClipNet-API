from fastapi import Body, Depends, HTTPException
from src.database import get_db
from src.schematics.user import UserCreateData
from src.models import User
from src.utils.hash import hash

def register(user_data: UserCreateData, db = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    new_user = User(
        username=user_data.username,
        password=hash(user_data.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

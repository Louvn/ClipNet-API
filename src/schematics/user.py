from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    token: str # For Permission-Only Logins

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True
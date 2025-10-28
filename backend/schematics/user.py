from pydantic import BaseModel, constr

class UserCreateData(BaseModel):
    username: str
    password: constr(min_length=8)
    token: str # For Permission-Only Logins

class UserOutData(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True
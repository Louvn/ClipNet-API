from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from .register import register
from .login import login
from src.schematics.user import UserOutData

router = APIRouter(tags=["authentification"])

router.add_api_route(
    "/register",
    register, 
    methods=["POST"], 
    response_model=UserOutData
)
router.add_api_route(
    "/login",
    login,
    methods=["POST"]
)
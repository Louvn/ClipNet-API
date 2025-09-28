from fastapi import APIRouter
from .register import register
from .login import login
from src.schematics.user import UserOut

router = APIRouter(tags=["authentification"])

router.add_api_route(
    "/register",
    register, 
    methods=["POST"], 
    response_model=UserOut
)
router.add_api_route(
    "/login",
    login,
    methods=["POST"]
)
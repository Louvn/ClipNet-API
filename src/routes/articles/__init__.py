from fastapi import APIRouter
from .create_article import create_article

router = APIRouter(tags=["articles"])

router.add_api_route(
    "/create-article",
    create_article,
    methods=["POST"]
)
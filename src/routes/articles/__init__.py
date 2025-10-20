from fastapi import APIRouter
from .create_article import create_article
from .edit_article import edit_article
from .get_article import get_article
from src.schematics.article import ArticleOutData
from src.schematics.revision import RevisionOutData

router = APIRouter(tags=["articles"])

router.add_api_route(
    "/create-article",
    create_article,
    methods=["POST"]
)

router.add_api_route(
    "/edit-article",
    edit_article,
    methods=["PUT"],
    response_model=RevisionOutData
)

router.add_api_route(
    "/get-article",
    get_article,
    methods=["GET"]
)
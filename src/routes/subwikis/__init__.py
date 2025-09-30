from fastapi import APIRouter
from .create_subwiki import create_subwiki
from src.schematics.subwiki import SubWikiOutData

router = APIRouter(tags=["subwikis"])

router.add_api_route(
    "/create-subwiki",
    create_subwiki, 
    methods=["POST"],
    response_model=SubWikiOutData
)
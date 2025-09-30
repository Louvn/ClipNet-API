from fastapi import Depends, HTTPException
from src.database import get_db
from src.schematics.subwiki import SubWikiCreateData
from src.models import SubWiki
from src.core.security.jwt_helpers import get_current_user

def create_subwiki(subwiki_data: SubWikiCreateData, db = Depends(get_db), user = Depends(get_current_user)):
    existing_subwiki = db.query(SubWiki).filter(SubWiki.name == subwiki_data.name).first()
    if existing_subwiki:
        raise HTTPException(status_code=400, detail="The provided name is already in use")

    new_subwiki = SubWiki(
        name = subwiki_data.name,
        owner = user
    )
    db.add(new_subwiki)
    db.commit()
    db.refresh(new_subwiki)

    return new_subwiki
from fastapi import Depends, HTTPException
from backend.core.security.jwt_helpers import get_current_user
from backend.database import get_db
from backend.schematics.article import ArticleGetData, ArticleOutData
from backend.schematics.revision import RevisionOutData
from backend.models import Article

def get_article(provided_infos = Depends(ArticleGetData), user = Depends(get_current_user), db = Depends(get_db)):
    "You can get the data of an Article via slug or id of the Article"
    if provided_infos.id is not None:
        article = db.query(Article).filter(Article.id == provided_infos.id).first()
    elif provided_infos.slug is not None:
        article = db.query(Article).filter(Article.slug == provided_infos.slug).first()
    
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    
    return {
        "article": ArticleOutData.model_validate(article, from_attributes=True),
        "current_revision": RevisionOutData.model_validate(article.current_revision, from_attributes=True)
    }
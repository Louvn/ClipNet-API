from fastapi import Depends, HTTPException
from sqlalchemy.orm import aliased
from sqlalchemy import and_
from src.database import get_db
from src.core.security.jwt_helpers import get_current_user
from src.core.slugs.generate_slug import generate_unique_slug
from src.schematics.article import ArticleCreateData
from src.models.article import Article
from src.models.subwiki import SubWiki
from src.models.revision import Revision

def create_article(article_data: ArticleCreateData, db = Depends(get_db), user = Depends(get_current_user)):
    rev = aliased(Revision)
    existing_article = (
        db.query(Article)
        .join(rev, Article.current_revision)
        .filter(
            and_(
                rev.name == article_data.name, 
                Article.subwiki_id == article_data.subwiki_id
            )
        )
        .first()
    )
    if existing_article:
        raise HTTPException(status_code=400, detail="Article does already exists")
    
    existing_subwiki = db.query(SubWiki).filter(SubWiki.id == article_data.subwiki_id).first()
    if not existing_subwiki:
        raise HTTPException(status_code=400, detail="A SubWiki with this ID does not exists")
    
    new_revision = Revision(
        name = article_data.name,
        content = article_data.content,
        change_summary = "created this article",
        user = user
    )

    new_article = Article(
        current_revision = new_revision,
        revisions = [new_revision],
        slug = "",
        op = user,
        subwiki = existing_subwiki
    )
    db.add_all([new_revision, new_article])
    db.flush()

    new_article.slug = generate_unique_slug(
        new_revision.name, 
        Article, 
        new_article.id
    )

    new_revision.article = new_article

    db.commit()
    db.refresh(new_article)
    db.refresh(new_revision)
    return [
        new_article, 
        new_revision,
        user
    ]
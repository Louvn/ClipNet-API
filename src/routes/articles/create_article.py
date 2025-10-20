from fastapi import Depends, HTTPException
from sqlalchemy.orm import aliased
from sqlalchemy import and_
from src.database import get_db
from src.core.security.jwt_helpers import get_current_user
from src.core.slugs.generate_slug import generate_unique_slug
from src.schematics.article import ArticleCreateData, ArticleOutData
from src.schematics.revision import RevisionOutData
from src.models.article import Article
from src.models.subwiki import SubWiki
from src.models.revision import Revision

def create_article(article_data: ArticleCreateData, db = Depends(get_db), user = Depends(get_current_user)):
    "Creating an Article will create the Article itself and the first Revision."
    # Avoid name conflicts in subwikis
    rev = aliased(Revision)
    existing_article_with_name = (
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
    if existing_article_with_name:
        raise HTTPException(status_code=400, detail="Article does already exists in this SubWiki")
    
    # Find the subwiki to create the article there
    existing_subwiki = db.query(SubWiki).filter(SubWiki.id == article_data.subwiki_id).first()
    if not existing_subwiki:
        raise HTTPException(status_code=400, detail="A SubWiki with this ID does not exists")
    
    # Create first revision
    new_revision = Revision(
        name = article_data.name,
        content = article_data.content,
        change_summary = "created this article",
        user = user
    )

    # Create Article
    new_article = Article(
        current_revision = new_revision,
        revisions = [new_revision],
        slug = "",
        op = user,
        subwiki = existing_subwiki
    )

    db.add_all([new_revision, new_article])
    db.flush()

    # Generate a slug
    new_article.slug = generate_unique_slug(
        new_revision.name, 
        Article, 
        new_article.id
    )

    new_revision.article = new_article

    db.commit()
    db.refresh(new_article)
    db.refresh(new_revision)
    
    return {
        "article": ArticleOutData.model_validate(new_article, from_attributes=True), 
        "current_revision": RevisionOutData.model_validate(new_revision, from_attributes=True)
    }
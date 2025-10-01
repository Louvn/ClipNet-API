import re
import unicodedata
from fastapi import Depends
from src.database import get_db

def generate_slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")

    text = re.sub(r'[^a-z0-9]+', '-', text.lower())
    text = text.strip("-")

    return text

def is_slug_unique(slug: str, sql_table) -> bool:
    db_gen = get_db()
    db = next(db_gen)
    existing_slug = db.query(sql_table).filter(sql_table.slug == slug).first()
    if not existing_slug:
        return True
    
    return False

def generate_unique_slug(text: str, sql_table, add_if_not_unique: str):
    slug = generate_slug(text)

    if is_slug_unique(slug, sql_table):
        return slug
    
    slug += add_if_not_unique
    return slug
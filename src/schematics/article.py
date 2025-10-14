from pydantic import BaseModel, constr

class ArticleCreateData(BaseModel):
    name: constr(min_length=1, max_length=50)
    content: str
    subwiki_id: int

class ArticleOutData(BaseModel):
    id: str
    name: str
    content: str
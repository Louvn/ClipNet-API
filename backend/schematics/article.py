from pydantic import BaseModel, constr, Field
from typing import Optional

class ArticleCreateData(BaseModel):
    name: constr(min_length=1, max_length=50)
    content: str

class ArticleOutData(BaseModel):
    id: int
    slug: str
    op_id: int

class ArticleGetData(BaseModel):
    id: Optional[int] = Field(None)
    slug: Optional[str] = Field(None)
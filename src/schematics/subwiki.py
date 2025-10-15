from pydantic import BaseModel, constr
from datetime import datetime

class SubWikiCreateData(BaseModel):
    name: constr(min_length=3, max_length=70)

class SubWikiOutData(BaseModel):
    name: str
    slug: str
    id: int
    created_at: datetime
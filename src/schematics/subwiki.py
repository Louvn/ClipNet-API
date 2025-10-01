from pydantic import BaseModel, constr

class SubWikiCreateData(BaseModel):
    name: constr(min_length=3, max_length=70)

class SubWikiOutData(BaseModel):
    name: str
    slug: str
    id: int
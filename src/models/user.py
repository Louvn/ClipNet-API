from ..database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .article import Article
from .revision import Revision

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    revisions = relationship("Revision", back_populates="user", foreign_keys=[Revision.user_id])
    articles = relationship("Article", back_populates="op", foreign_keys=[Article.op_id])
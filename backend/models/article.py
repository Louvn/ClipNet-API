from ..database import Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from .revision import Revision

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    slug = Column(String(50), index=True)
    current_revision_id = Column(Integer, ForeignKey("revisions.id"))
    op_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    revisions = relationship("Revision", foreign_keys=[Revision.article_id], back_populates="article")
    current_revision = relationship("Revision", uselist=False, foreign_keys=[current_revision_id], post_update=True) # post_update=True avoids circular dependency errors
    op = relationship("User", foreign_keys=[op_id], back_populates="articles")
from ..database import Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Revision(Base):
    __tablename__ = "revisions"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    content = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    change_summary = Column(String(255))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    article_id = Column(Integer, ForeignKey("articles.id", ondelete="CASCADE"))

    article = relationship("Article", foreign_keys=[article_id], back_populates="revisions")
    user = relationship("User", foreign_keys=[user_id], back_populates="revisions")
    
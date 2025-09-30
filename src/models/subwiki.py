from ..database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class SubWiki(Base):
    __tablename__ = "subwikis"
    id = Column(Integer, primary_key=True)
    name = Column(String(70), unique=True)
    slug = Column(String(70), unique=True, index=True, nullable=True) # TODO: Generate!
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    owner = relationship("User")
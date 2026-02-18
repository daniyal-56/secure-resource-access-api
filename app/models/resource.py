from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    is_protected = Column(Boolean, default=True)
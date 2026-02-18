from sqlalchemy import Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    # Primary Key for the User entity
    id = Column(Integer, primary_key=True, index=True)
    
    username = Column(String, unique=True, index=True)
    
    hashed_password = Column(String)
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Index
from datetime import datetime
from app.database import Base

class AccessRequest(Base):
    __tablename__ = "access_requests"
    
    id = Column(Integer, primary_key=True, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    resource_id = Column(Integer, ForeignKey("resources.id"), index=True)
    
    status = Column(String, default="pending", index=True)
    
    requested_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True, index=True)

    __table_args__ = (
        Index('ix_user_resource_active', "user_id", "resource_id", "status"),
    )
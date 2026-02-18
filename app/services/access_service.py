from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import HTTPException
from app.models.access_request import AccessRequest
from app.config import settings

class AccessService:
    @staticmethod
    def get_active_access(db: Session, user_id: int, resource_id: int):
        """
        Constraint Check: A user cannot have more than one active access 
        to the same resource[cite: 40].
        """
        return db.query(AccessRequest).filter(
            AccessRequest.user_id == user_id,
            AccessRequest.resource_id == resource_id,
            AccessRequest.status == "approved",
            AccessRequest.expires_at > datetime.utcnow()
        ).first()

    @staticmethod
    def process_approval(db: Session, request_id: int):
        """
        Handles Access approval and automatic expiration logic[cite: 28, 29].
        Uses 'with_for_update' to handle race conditions during simultaneous 
        approvals[cite: 42].
        """
        req = db.query(AccessRequest).with_for_update().filter(AccessRequest.id == request_id).first()
        
        if not req:
            raise HTTPException(status_code=404, detail="Access request not found")
        
        if req.status != "pending":
            raise HTTPException(status_code=400, detail="Request has already been processed")

        req.status = "approved"
        # Access expires automatically after a configurable time window [cite: 39]
        req.expires_at = datetime.utcnow() + timedelta(seconds=settings.DEFAULT_ACCESS_DURATION_SECONDS)
        
        db.commit()
        db.refresh(req)
        return req

    @staticmethod
    def validate_token_usage(db: Session, user_id: int, resource_id: int):
        """
        Ensures expired access is not usable even if the token is presented[cite: 41].
        """
        access = db.query(AccessRequest).filter(
            AccessRequest.user_id == user_id,
            AccessRequest.resource_id == resource_id,
            AccessRequest.status == "approved"
        ).first()

        if not access or access.expires_at < datetime.utcnow():
            if access:
                access.status = "expired"
                db.commit()
            raise HTTPException(status_code=403, detail="Access expired or unauthorized")
        
        return True
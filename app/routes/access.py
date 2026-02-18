from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.access_service import AccessService
from app.schemas.access import AccessRequestOut
from app.models.access_request import AccessRequest

router = APIRouter(prefix="/access", tags=["Access Management"])

@router.post("/request/{resource_id}", response_model=AccessRequestOut)
def request_resource_access(resource_id: int, user_id: int, db: Session = Depends(get_db)):
    if AccessService.get_active_access(db, user_id, resource_id):
        raise HTTPException(status_code=400, detail="Active access already exists")
    
    new_request = AccessRequest(user_id=user_id, resource_id=resource_id)
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

@router.post("/approve/{request_id}", response_model=AccessRequestOut)
def approve_request(request_id: int, db: Session = Depends(get_db)):
    return AccessService.process_approval(db, request_id)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.resource import Resource
from app.schemas.resource import ResourceCreate, ResourceOut

router = APIRouter(prefix="/resources", tags=["Resources"])

@router.post("/", response_model=ResourceOut)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    new_res = Resource(**resource.dict())
    db.add(new_res)
    db.commit()
    db.refresh(new_res)
    return new_res

@router.get("/")
def list_resources(db: Session = Depends(get_db)):
    return db.query(Resource).all()
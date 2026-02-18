from pydantic import BaseModel

class ResourceCreate(BaseModel):
    name: str
    description: str
    is_protected: bool = True

class ResourceOut(ResourceCreate):
    id: int
    model_config = {"from_attributes": True}
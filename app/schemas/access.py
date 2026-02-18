from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AccessRequestOut(BaseModel):
    id: int
    user_id: int
    resource_id: int
    status: str
    expires_at: Optional[datetime]
    
    model_config = {"from_attributes": True}
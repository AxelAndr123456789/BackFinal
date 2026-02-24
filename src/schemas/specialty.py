from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SpecialtyBase(BaseModel):
    name: str
    description: Optional[str] = None
    icon: Optional[str] = None


class SpecialtyCreate(SpecialtyBase):
    pass


class SpecialtyUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None


class SpecialtyResponse(SpecialtyBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

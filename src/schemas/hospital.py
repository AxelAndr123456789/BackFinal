from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class HospitalInfoBase(BaseModel):
    name: str
    description: str
    mission: Optional[str] = None
    vision: Optional[str] = None
    history: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None


class HospitalInfoCreate(HospitalInfoBase):
    pass


class HospitalInfoUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    mission: Optional[str] = None
    vision: Optional[str] = None
    history: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None


class HospitalInfoResponse(HospitalInfoBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class DirectorBase(BaseModel):
    name: str
    last_name: str
    title: str
    bio: Optional[str] = None
    photo_url: Optional[str] = None


class DirectorCreate(DirectorBase):
    pass


class DirectorUpdate(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    bio: Optional[str] = None
    photo_url: Optional[str] = None


class DirectorResponse(DirectorBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class ServiceBase(BaseModel):
    name: str
    description: str
    icon: Optional[str] = None
    is_highlighted: bool = False


class ServiceCreate(ServiceBase):
    pass


class ServiceUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    is_highlighted: Optional[bool] = None


class ServiceResponse(ServiceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class LocationBase(BaseModel):
    address: str
    latitude: float
    longitude: float
    google_maps_url: Optional[str] = None


class LocationCreate(LocationBase):
    pass


class LocationUpdate(BaseModel):
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    google_maps_url: Optional[str] = None


class LocationResponse(LocationBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class DoctorBase(BaseModel):
    name: str
    last_name: str
    specialty_id: int
    license_number: str
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    years_experience: Optional[int] = None


class DoctorCreate(DoctorBase):
    pass


class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    last_name: Optional[str] = None
    specialty_id: Optional[int] = None
    license_number: Optional[str] = None
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    years_experience: Optional[int] = None


class DoctorResponse(DoctorBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class DoctorWithSpecialty(BaseModel):
    id: int
    name: str
    last_name: str
    specialty_id: int
    specialty_name: str
    license_number: str
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    years_experience: Optional[int] = None

    class Config:
        from_attributes = True


class DoctorAvailabilityResponse(BaseModel):
    doctor_id: int
    has_availability: bool
    schedule: Optional[dict] = None

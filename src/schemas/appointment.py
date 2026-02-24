from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date, time


class AppointmentBase(BaseModel):
    doctor_id: int
    specialty_id: int
    date: date
    time: time
    reason: Optional[str] = None
    notes: Optional[str] = None


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentUpdate(BaseModel):
    date: Optional[date] = None
    time: Optional[time] = None
    reason: Optional[str] = None
    notes: Optional[str] = None
    status: Optional[str] = None


class AppointmentResponse(AppointmentBase):
    id: int
    user_id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class AppointmentWithDetails(BaseModel):
    id: int
    user_id: int
    doctor_id: int
    doctor_name: str
    doctor_last_name: str
    specialty_id: int
    specialty_name: str
    date: date
    time: time
    reason: Optional[str] = None
    notes: Optional[str] = None
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class AppointmentCancelResponse(BaseModel):
    message: str
    appointment: AppointmentResponse


class UpcomingAppointmentResponse(BaseModel):
    id: int
    doctor_name: str
    specialty_name: str
    date: str
    time: str

    class Config:
        from_attributes = True

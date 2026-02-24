from pydantic import BaseModel
from typing import Optional, List
from datetime import date, time


class AvailabilitySlotBase(BaseModel):
    doctor_id: int
    date: date
    start_time: time
    end_time: time
    is_available: bool = True


class AvailabilitySlotCreate(AvailabilitySlotBase):
    pass


class AvailabilitySlotResponse(AvailabilitySlotBase):
    id: int

    class Config:
        from_attributes = True


class DateAvailabilityResponse(BaseModel):
    doctor_id: int
    month: int
    year: int
    available_dates: List[str]


class TimeSlotsResponse(BaseModel):
    doctor_id: int
    date: str
    morning_slots: List[str]
    afternoon_slots: List[str]


class CheckAvailabilityRequest(BaseModel):
    doctor_id: int
    date: str
    time: str


class CheckAvailabilityResponse(BaseModel):
    available: bool
    doctor_id: int
    date: str
    time: str
    message: str

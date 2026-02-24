from fastapi import APIRouter, Query
from src.schemas.availability import (
    DateAvailabilityResponse,
    TimeSlotsResponse,
    CheckAvailabilityResponse,
)
from src.services.availability_service import availability_service

router = APIRouter(prefix="/availability", tags=["Availability"])


@router.get("/doctors/{doctor_id}/dates", response_model=DateAvailabilityResponse)
def get_available_dates(
    doctor_id: int,
    month: int = Query(..., description="Mes (1-12)"),
    year: int = Query(..., description="Año"),
):
    return availability_service.get_available_dates(doctor_id, month, year)


@router.get("/doctors/{doctor_id}/slots", response_model=TimeSlotsResponse)
def get_time_slots(
    doctor_id: int, date: str = Query(..., description="Fecha (YYYY-MM-DD)")
):
    return availability_service.get_time_slots(doctor_id, date)


@router.get("/check", response_model=CheckAvailabilityResponse)
def check_availability(
    doctor_id: int = Query(...), date: str = Query(...), time: str = Query(...)
):
    return availability_service.check_availability(doctor_id, date, time)

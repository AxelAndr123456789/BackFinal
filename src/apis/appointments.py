from fastapi import APIRouter, HTTPException, Header, Query
from typing import List, Optional
from src.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse,
    AppointmentWithDetails,
    AppointmentCancelResponse,
    UpcomingAppointmentResponse,
)
from src.services.appointment_service import appointment_service
from src.config.database import get_all
    
router = APIRouter(prefix="/appointments", tags=["Appointments"])


@router.post("", response_model=AppointmentResponse)
def create_appointment(data: AppointmentCreate, x_user_id: int = Header(default=1)):
    return appointment_service.create_appointment(x_user_id, data)


@router.get("/me", response_model=List[AppointmentWithDetails])
def get_my_appointments(
    x_user_id: int = Header(default=1),
    status: Optional[str] = Query(None, description="Estado de la cita"),
):
    return appointment_service.get_user_appointments(x_user_id, status)


@router.get("/history", response_model=List[AppointmentWithDetails])
def get_appointment_history(x_user_id: int = Header(default=1)):
    return appointment_service.get_user_appointments(x_user_id, status="completed")


@router.get("/booked-slots", response_model=List[dict])
def get_booked_slots():
    """Returns all booked time slots (date, time, specialty) without user info"""
    query = """
        SELECT c.fecha, c.hora, e.nombre as especialidad
        FROM citas c
        JOIN especialidades e ON c.especialidad_id = e.id
        WHERE c.estado = 'programada'
    """
    results = get_all(query)
    return results


@router.get("/{appointment_id}", response_model=AppointmentWithDetails)
def get_appointment_by_id(appointment_id: int):
    appointment = appointment_service.get_appointment_by_id(appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return appointment


@router.put("/{appointment_id}/cancel", response_model=AppointmentCancelResponse)
def cancel_appointment(appointment_id: int):
    try:
        return appointment_service.cancel_appointment(appointment_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/upcoming", response_model=UpcomingAppointmentResponse)
def get_upcoming_appointment(x_user_id: int = Header(default=1)):
    return appointment_service.get_upcoming_appointment(x_user_id)

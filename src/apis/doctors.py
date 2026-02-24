from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas.doctor import (
    DoctorResponse,
    DoctorWithSpecialty,
    DoctorAvailabilityResponse,
)
from src.services.doctor_service import doctor_service

router = APIRouter(prefix="/doctors", tags=["Doctors"])


@router.get("/by-specialty/{specialty_id}", response_model=List[DoctorWithSpecialty])
def get_doctors_by_specialty(specialty_id: int):
    return doctor_service.get_doctors_by_specialty(specialty_id)


@router.get("/{doctor_id}", response_model=DoctorResponse)
def get_doctor_by_id(doctor_id: int):
    doctor = doctor_service.get_doctor_by_id(doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor no encontrado")
    return doctor


@router.get("", response_model=List[DoctorResponse])
def get_all_doctors():
    return doctor_service.get_all_doctors()


@router.get("/{doctor_id}/availability", response_model=DoctorAvailabilityResponse)
def get_doctor_availability(doctor_id: int):
    return doctor_service.get_doctor_availability(doctor_id)

from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas.hospital import (
    HospitalInfoResponse,
    DirectorResponse,
    ServiceResponse,
    LocationResponse,
)
from src.services.hospital_service import hospital_service

router = APIRouter(prefix="/hospital", tags=["Hospital"])


@router.get("/info", response_model=HospitalInfoResponse)
def get_hospital_info():
    info = hospital_service.get_hospital_info()
    if not info:
        raise HTTPException(
            status_code=404, detail="Información del hospital no encontrada"
        )
    return info


@router.get("/director", response_model=DirectorResponse)
def get_director():
    director = hospital_service.get_director()
    if not director:
        raise HTTPException(status_code=404, detail="Director no encontrado")
    return director


@router.get("/services", response_model=List[ServiceResponse])
def get_services():
    return hospital_service.get_services()


@router.get("/location", response_model=LocationResponse)
def get_location():
    location = hospital_service.get_location()
    if not location:
        raise HTTPException(status_code=404, detail="Ubicación no encontrada")
    return location

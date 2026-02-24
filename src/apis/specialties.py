from fastapi import APIRouter, HTTPException, Query
from typing import List
from src.schemas.specialty import SpecialtyResponse
from src.services.specialty_service import specialty_service

router = APIRouter(prefix="/specialties", tags=["Specialties"])


@router.get("", response_model=List[SpecialtyResponse])
def get_all_specialties():
    return specialty_service.get_all_specialties()


@router.get("/{specialty_id}", response_model=SpecialtyResponse)
def get_specialty_by_id(specialty_id: int):
    specialty = specialty_service.get_specialty_by_id(specialty_id)
    if not specialty:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return specialty


@router.get("/search", response_model=List[SpecialtyResponse])
def search_specialties(q: str = Query(..., description="Texto de búsqueda")):
    return specialty_service.search_specialties(q)

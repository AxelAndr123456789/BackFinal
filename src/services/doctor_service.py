from typing import List, Optional
from src.schemas.doctor import (
    DoctorResponse,
    DoctorWithSpecialty,
    DoctorAvailabilityResponse,
)
from src.repositories.doctor_repository import doctor_repo


class DoctorService:
    def get_doctors_by_specialty(self, specialty_id: int) -> list[DoctorWithSpecialty]:
        return doctor_repo.get_by_specialty(specialty_id)

    def get_doctor_by_id(self, doctor_id: int) -> Optional[DoctorResponse]:
        return doctor_repo.get_by_id(doctor_id)

    def get_all_doctors(self) -> list[DoctorResponse]:
        return doctor_repo.get_all()

    def get_doctor_availability(self, doctor_id: int) -> DoctorAvailabilityResponse:
        return doctor_repo.get_availability(doctor_id)


doctor_service = DoctorService()

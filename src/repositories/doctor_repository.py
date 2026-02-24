from typing import Optional, List
from src.schemas.doctor import (
    DoctorCreate,
    DoctorResponse,
    DoctorWithSpecialty,
    DoctorAvailabilityResponse,
)
from src.config.database import get_one, get_all


class DoctorRepository:
    def get_by_specialty(self, specialty_id: int) -> List[DoctorWithSpecialty]:
        query = """
            SELECT d.id, d.nombre, d.apellido, d.especialidad_id, d.licencia, d.biografia, d.foto_url, d.anos_experiencia,
                   e.nombre as nombre_especialidad
            FROM doctores d
            JOIN especialidades e ON d.especialidad_id = e.id
            WHERE d.especialidad_id = %s
        """
        results = get_all(query, (specialty_id,))
        return [
            DoctorWithSpecialty(
                id=r["id"],
                name=r["nombre"],
                last_name=r["apellido"],
                specialty_id=r["especialidad_id"],
                specialty_name=r["nombre_especialidad"],
                license_number=r["licencia"],
                bio=r.get("biografia"),
                photo_url=r.get("foto_url"),
                years_experience=r.get("anos_experiencia"),
            )
            for r in results
        ]

    def get_by_id(self, doctor_id: int) -> Optional[DoctorResponse]:
        query = "SELECT * FROM doctores WHERE id = %s"
        result = get_one(query, (doctor_id,))
        if result:
            return DoctorResponse(
                id=result["id"],
                name=result["nombre"],
                last_name=result["apellido"],
                specialty_id=result["especialidad_id"],
                license_number=result["licencia"],
                bio=result.get("biografia"),
                photo_url=result.get("foto_url"),
                years_experience=result.get("anos_experiencia"),
                created_at=result["created_at"],
            )
        return None

    def get_all(self) -> List[DoctorResponse]:
        query = "SELECT * FROM doctores ORDER BY id"
        results = get_all(query)
        return [
            DoctorResponse(
                id=r["id"],
                name=r["nombre"],
                last_name=r["apellido"],
                specialty_id=r["especialidad_id"],
                license_number=r["licencia"],
                bio=r.get("biografia"),
                photo_url=r.get("foto_url"),
                years_experience=r.get("anos_experiencia"),
                created_at=r["created_at"],
            )
            for r in results
        ]

    def get_availability(self, doctor_id: int) -> DoctorAvailabilityResponse:
        return DoctorAvailabilityResponse(
            doctor_id=doctor_id,
            has_availability=True,
            schedule={
                "monday": "8:00-17:00",
                "tuesday": "8:00-17:00",
                "wednesday": "8:00-17:00",
                "thursday": "8:00-17:00",
                "friday": "8:00-14:00",
            },
        )


doctor_repo = DoctorRepository()

from datetime import datetime
from typing import Optional, List
from src.schemas.hospital import (
    HospitalInfoCreate,
    HospitalInfoUpdate,
    HospitalInfoResponse,
    DirectorCreate,
    DirectorUpdate,
    DirectorResponse,
    ServiceCreate,
    ServiceUpdate,
    ServiceResponse,
    LocationCreate,
    LocationUpdate,
    LocationResponse,
)


class HospitalRepository:
    def __init__(self):
        self._info: Optional[dict] = None
        self._director: Optional[dict] = None
        self._services: List[dict] = []
        self._location: Optional[dict] = None
        self._seed_data()

    def _seed_data(self):
        self._info = {
            "id": 1,
            "name": "Hospital HealthConnect",
            "description": "Centro médico de atención integral con tecnología de vanguardia",
            "mission": "Brindar atención médica de calidad a toda la comunidad",
            "vision": "Ser el hospital de referencia en la región",
            "history": "Fundado en 2010, el Hospital HealthConnect ha crecido hasta convertirse en un centro médico de referencia",
            "phone": "+52 (555) 123-4567",
            "email": "contacto@healthconnect.com",
            "address": "Av. Principal #123, Ciudad de México",
            "created_at": datetime.now(),
        }
        self._director = {
            "id": 1,
            "name": "Christian",
            "last_name": "Matamoros",
            "title": "Director General",
            "bio": "Dr. Christian Matamoros con más de 20 años de experiencia en administración hospitalaria",
            "photo_url": None,
            "created_at": datetime.now(),
        }
        services = [
            {
                "name": "Urgencias",
                "description": "Atención de emergencias 24/7",
                "icon": "emergency",
                "is_highlighted": True,
            },
            {
                "name": "Cirugía",
                "description": "Quirófanos equipados con tecnología de última generación",
                "icon": "surgery",
                "is_highlighted": True,
            },
            {
                "name": "Laboratorio",
                "description": "Análisis clínicos y estudios diagnósticos",
                "icon": "lab",
                "is_highlighted": True,
            },
            {
                "name": "Imagenología",
                "description": "Rayos X, resonancia magnética, tomografía",
                "icon": "imaging",
                "is_highlighted": True,
            },
        ]
        for svc in services:
            self._services.append(
                {"id": len(self._services) + 1, **svc, "created_at": datetime.now()}
            )
        self._location = {
            "id": 1,
            "address": "Av. Principal #123, Ciudad de México",
            "latitude": 19.4326,
            "longitude": -99.1332,
            "google_maps_url": "https://maps.google.com/?q=19.4326,-99.1332",
            "created_at": datetime.now(),
        }

    def get_info(self) -> Optional[HospitalInfoResponse]:
        if self._info:
            return HospitalInfoResponse(**self._info)
        return None

    def get_director(self) -> Optional[DirectorResponse]:
        if self._director:
            return DirectorResponse(**self._director)
        return None

    def get_services(self) -> List[ServiceResponse]:
        return [ServiceResponse(**s) for s in self._services]

    def get_location(self) -> Optional[LocationResponse]:
        if self._location:
            return LocationResponse(**self._location)
        return None


hospital_repo = HospitalRepository()

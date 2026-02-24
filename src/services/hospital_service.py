from typing import List, Optional
from src.schemas.hospital import (
    HospitalInfoResponse,
    DirectorResponse,
    ServiceResponse,
    LocationResponse,
)
from src.repositories.hospital_repository import hospital_repo


class HospitalService:
    def get_hospital_info(self) -> Optional[HospitalInfoResponse]:
        return hospital_repo.get_info()

    def get_director(self) -> Optional[DirectorResponse]:
        return hospital_repo.get_director()

    def get_services(self) -> list[ServiceResponse]:
        return hospital_repo.get_services()

    def get_location(self) -> Optional[LocationResponse]:
        return hospital_repo.get_location()


hospital_service = HospitalService()

from typing import List, Optional
from src.schemas.specialty import SpecialtyResponse
from src.repositories.specialty_repository import specialty_repo


class SpecialtyService:
    def get_all_specialties(self) -> list[SpecialtyResponse]:
        return specialty_repo.get_all()

    def get_specialty_by_id(self, specialty_id: int) -> Optional[SpecialtyResponse]:
        return specialty_repo.get_by_id(specialty_id)

    def search_specialties(self, query: str) -> list[SpecialtyResponse]:
        return specialty_repo.search(query)


specialty_service = SpecialtyService()

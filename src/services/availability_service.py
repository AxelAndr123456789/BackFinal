from src.schemas.availability import (
    DateAvailabilityResponse,
    TimeSlotsResponse,
    CheckAvailabilityResponse,
)
from src.repositories.availability_repository import availability_repo


class AvailabilityService:
    def get_available_dates(
        self, doctor_id: int, month: int, year: int
    ) -> DateAvailabilityResponse:
        return availability_repo.get_dates(doctor_id, month, year)

    def get_time_slots(self, doctor_id: int, date: str) -> TimeSlotsResponse:
        return availability_repo.get_slots(doctor_id, date)

    def check_availability(
        self, doctor_id: int, date: str, time: str
    ) -> CheckAvailabilityResponse:
        return availability_repo.check_availability(doctor_id, date, time)


availability_service = AvailabilityService()

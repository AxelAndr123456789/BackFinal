from typing import List
from src.schemas.availability import (
    DateAvailabilityResponse,
    TimeSlotsResponse,
    CheckAvailabilityResponse,
)
from src.config.database import get_one, get_all


class AvailabilityRepository:
    def get_dates(
        self, doctor_id: int, month: int, year: int
    ) -> DateAvailabilityResponse:
        query = """
            SELECT DISTINCT fecha FROM disponibilidad
            WHERE doctor_id = %s
            AND EXTRACT(MONTH FROM fecha) = %s
            AND EXTRACT(YEAR FROM fecha) = %s
            AND esta_disponible = TRUE
            ORDER BY fecha
        """
        results = get_all(query, (doctor_id, month, year))
        available_dates = [str(r["fecha"]) for r in results]

        if not available_dates:
            available_dates = [
                "2026-02-10",
                "2026-02-12",
                "2026-02-15",
                "2026-02-18",
                "2026-02-20",
                "2026-02-22",
            ]

        return DateAvailabilityResponse(
            doctor_id=doctor_id, month=month, year=year, available_dates=available_dates
        )

    def get_slots(self, doctor_id: int, date: str) -> TimeSlotsResponse:
        query = """
            SELECT hora_inicio, hora_fin FROM disponibilidad
            WHERE doctor_id = %s
            AND fecha = %s
            AND esta_disponible = TRUE
            ORDER BY hora_inicio
        """
        results = get_all(query, (doctor_id, date))

        morning_slots = []
        afternoon_slots = []

        for r in results:
            start_hour = r["hora_inicio"].hour
            time_str = r["hora_inicio"].strftime("%H:%M")
            if start_hour < 12:
                morning_slots.append(time_str)
            else:
                afternoon_slots.append(time_str)

        if not morning_slots:
            morning_slots = [
                "08:00",
                "08:30",
                "09:00",
                "09:30",
                "10:00",
                "10:30",
                "11:00",
                "11:30",
            ]
        if not afternoon_slots:
            afternoon_slots = ["14:00", "14:30", "15:00", "15:30", "16:00", "16:30"]

        return TimeSlotsResponse(
            doctor_id=doctor_id,
            date=date,
            morning_slots=morning_slots,
            afternoon_slots=afternoon_slots,
        )

    def check_availability(
        self, doctor_id: int, date: str, time: str
    ) -> CheckAvailabilityResponse:
        query = """
            SELECT * FROM disponibilidad
            WHERE doctor_id = %s
            AND fecha = %s
            AND hora_inicio <= %s
            AND hora_fin > %s
            AND esta_disponible = TRUE
        """
        result = get_one(query, (doctor_id, date, time, time))

        return CheckAvailabilityResponse(
            available=result is not None,
            doctor_id=doctor_id,
            date=date,
            time=time,
            message="El horario está disponible"
            if result
            else "El horario no está disponible",
        )


availability_repo = AvailabilityRepository()

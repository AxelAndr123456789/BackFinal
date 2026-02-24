from typing import List, Optional
from src.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse,
    AppointmentWithDetails,
    AppointmentCancelResponse,
    UpcomingAppointmentResponse,
)
from src.repositories.appointment_repository import appointment_repo


class AppointmentService:
    def create_appointment(
        self, user_id: int, data: AppointmentCreate
    ) -> AppointmentResponse:
        return appointment_repo.create_appointment(user_id, data)

    def get_user_appointments(
        self, user_id: int, status: Optional[str] = None
    ) -> list[AppointmentWithDetails]:
        return appointment_repo.get_user_appointments(user_id, status)

    def get_appointment_by_id(
        self, appointment_id: int
    ) -> Optional[AppointmentWithDetails]:
        return appointment_repo.get_by_id(appointment_id)

    def cancel_appointment(self, appointment_id: int) -> AppointmentCancelResponse:
        appointment = appointment_repo.cancel_appointment(appointment_id)
        if not appointment:
            raise ValueError("Cita no encontrada")
        return AppointmentCancelResponse(
            message="Cita cancelada exitosamente", appointment=appointment
        )

    def get_upcoming_appointment(
        self, user_id: int
    ) -> Optional[UpcomingAppointmentResponse]:
        return appointment_repo.get_upcoming(user_id)


appointment_service = AppointmentService()

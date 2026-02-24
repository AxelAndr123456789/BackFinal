from typing import Optional, List
from datetime import datetime
from src.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse,
    AppointmentWithDetails,
    UpcomingAppointmentResponse,
)
from src.config.database import get_one, get_all, execute


class AppointmentRepository:
    def create_appointment(
        self, user_id: int, data: AppointmentCreate
    ) -> AppointmentResponse:
        query = """
            INSERT INTO citas (usuario_id, doctor_id, especialidad_id, fecha, hora, estado)
            VALUES (%s, %s, %s, %s, %s, 'programada')
            RETURNING id, usuario_id, doctor_id, especialidad_id, fecha, hora, estado, created_at
        """
        result = get_one(
            query,
            (
                user_id,
                data.doctor_id,
                data.specialty_id,
                data.date,
                data.time,
            ),
        )

        return AppointmentResponse(
            id=result["id"],
            user_id=result["usuario_id"],
            doctor_id=result["doctor_id"],
            specialty_id=result["especialidad_id"],
            date=result["fecha"],
            time=result["hora"],
            reason=None,
            notes=None,
            status=result["estado"],
            created_at=result["created_at"],
        )

    def get_user_appointments(
        self, user_id: int, status: Optional[str] = None
    ) -> List[AppointmentWithDetails]:
        if status:
            query = """
                SELECT c.id, c.usuario_id, c.doctor_id, c.especialidad_id, c.fecha, c.hora, c.estado, c.created_at,
                       d.nombre as nombre_doctor, d.apellido as apellido_doctor,
                       e.nombre as nombre_especialidad
                FROM citas c
                JOIN doctores d ON c.doctor_id = d.id
                JOIN especialidades e ON c.especialidad_id = e.id
                WHERE c.usuario_id = %s AND c.estado = %s
                ORDER BY c.fecha DESC
            """
            results = get_all(query, (user_id, status))
        else:
            query = """
                SELECT c.id, c.usuario_id, c.doctor_id, c.especialidad_id, c.fecha, c.hora, c.estado, c.created_at,
                       d.nombre as nombre_doctor, d.apellido as apellido_doctor,
                       e.nombre as nombre_especialidad
                FROM citas c
                JOIN doctores d ON c.doctor_id = d.id
                JOIN especialidades e ON c.especialidad_id = e.id
                WHERE c.usuario_id = %s
                ORDER BY c.fecha DESC
            """
            results = get_all(query, (user_id,))

        return [
            AppointmentWithDetails(
                id=r["id"],
                user_id=r["usuario_id"],
                doctor_id=r["doctor_id"],
                doctor_name=r["nombre_doctor"],
                doctor_last_name=r["apellido_doctor"],
                specialty_id=r["especialidad_id"],
                specialty_name=r["nombre_especialidad"],
                date=r["fecha"],
                time=r["hora"],
                reason=None,
                notes=None,
                status=r["estado"],
                created_at=r["created_at"],
            )
            for r in results
        ]

    def get_by_id(self, appointment_id: int) -> Optional[AppointmentWithDetails]:
        query = """
            SELECT c.id, c.usuario_id, c.doctor_id, c.especialidad_id, c.fecha, c.hora, c.estado, c.created_at,
                   d.nombre as nombre_doctor, d.apellido as apellido_doctor,
                   e.nombre as nombre_especialidad
            FROM citas c
            JOIN doctores d ON c.doctor_id = d.id
            JOIN especialidades e ON c.especialidad_id = e.id
            WHERE c.id = %s
        """
        result = get_one(query, (appointment_id,))

        if result:
            return AppointmentWithDetails(
                id=result["id"],
                user_id=result["usuario_id"],
                doctor_id=result["doctor_id"],
                doctor_name=result["nombre_doctor"],
                doctor_last_name=result["apellido_doctor"],
                specialty_id=result["especialidad_id"],
                specialty_name=result["nombre_especialidad"],
                date=result["fecha"],
                time=result["hora"],
                reason=None,
                notes=None,
                status=result["estado"],
                created_at=result["created_at"],
            )
        return None

    def cancel_appointment(self, appointment_id: int) -> Optional[AppointmentResponse]:
        query = """
            UPDATE citas SET estado = 'cancelada', updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
            RETURNING id, usuario_id, doctor_id, especialidad_id, fecha, hora, estado, created_at
        """
        result = get_one(query, (appointment_id,))

        if result:
            return AppointmentResponse(
                id=result["id"],
                user_id=result["usuario_id"],
                doctor_id=result["doctor_id"],
                specialty_id=result["especialidad_id"],
                date=result["fecha"],
                time=result["hora"],
                reason=None,
                notes=None,
                status=result["estado"],
                created_at=result["created_at"],
            )
        return None

    def get_upcoming(self, user_id: int) -> Optional[UpcomingAppointmentResponse]:
        query = """
            SELECT c.id, c.fecha, c.hora,
                   d.nombre as nombre_doctor, d.apellido as apellido_doctor,
                   e.nombre as nombre_especialidad
            FROM citas c
            JOIN doctores d ON c.doctor_id = d.id
            JOIN especialidades e ON c.especialidad_id = e.id
            WHERE c.usuario_id = %s AND c.estado = 'programada' AND c.fecha >= CURRENT_DATE
            ORDER BY c.fecha ASC
            LIMIT 1
        """
        result = get_one(query, (user_id,))

        if result:
            return UpcomingAppointmentResponse(
                id=result["id"],
                doctor_name=f"{result['nombre_doctor']} {result['apellido_doctor']}",
                specialty_name=result["nombre_especialidad"],
                date=str(result["fecha"]),
                time=str(result["hora"]),
            )
        return None


appointment_repo = AppointmentRepository()

from typing import Optional, List
from src.schemas.specialty import SpecialtyCreate, SpecialtyResponse
from src.config.database import get_one, get_all, execute


class SpecialtyRepository:
    def get_all(self) -> List[SpecialtyResponse]:
        query = "SELECT * FROM especialidades ORDER BY id"
        results = get_all(query)
        return [
            SpecialtyResponse(
                id=r["id"],
                name=r["nombre"],
                description=r.get("descripcion"),
                icon=r.get("icono"),
                created_at=r["created_at"],
            )
            for r in results
        ]

    def get_by_id(self, specialty_id: int) -> Optional[SpecialtyResponse]:
        query = "SELECT * FROM especialidades WHERE id = %s"
        result = get_one(query, (specialty_id,))
        if result:
            return SpecialtyResponse(
                id=result["id"],
                name=result["nombre"],
                description=result.get("descripcion"),
                icon=result.get("icono"),
                created_at=result["created_at"],
            )
        return None

    def search(self, query_str: str) -> List[SpecialtyResponse]:
        query = "SELECT * FROM especialidades WHERE LOWER(nombre) LIKE %s"
        results = get_all(query, (f"%{query_str.lower()}%",))
        return [
            SpecialtyResponse(
                id=r["id"],
                name=r["nombre"],
                description=r.get("descripcion"),
                icon=r.get("icono"),
                created_at=r["created_at"],
            )
            for r in results
        ]

    def create(self, data: SpecialtyCreate) -> SpecialtyResponse:
        query = """
            INSERT INTO especialidades (nombre, descripcion, icono)
            VALUES (%s, %s, %s)
            RETURNING id, nombre, descripcion, icono, created_at
        """
        result = get_one(query, (data.name, data.description, data.icon))
        return SpecialtyResponse(
            id=result["id"],
            name=result["nombre"],
            description=result.get("descripcion"),
            icon=result.get("icono"),
            created_at=result["created_at"],
        )


specialty_repo = SpecialtyRepository()

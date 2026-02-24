from typing import Optional
from src.schemas.auth import UserCreate, UserUpdate, UserResponse
from src.config.database import get_one, get_all, execute
import logging

logger = logging.getLogger(__name__)


class UserRepository:
    def create_user(self, user_data: UserCreate) -> UserResponse:
        try:
            query = """
                INSERT INTO usuarios (email, nombre, apellido, telefono, fecha_nacimiento, genero, password)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id, email, nombre, apellido, telefono, fecha_nacimiento, genero, created_at
            """
            params = (
                user_data.email,
                user_data.name,
                user_data.last_name,
                user_data.phone,
                user_data.date_of_birth,
                user_data.gender,
                user_data.password,
            )
            result = get_one(query, params)

            if result is None:
                raise Exception("No se pudo insertar el usuario")

            return UserResponse(
                id=result["id"],
                email=result["email"],
                name=result["nombre"],
                last_name=result["apellido"],
                phone=result.get("telefono"),
                date_of_birth=str(result.get("fecha_nacimiento"))
                if result.get("fecha_nacimiento")
                else None,
                gender=result.get("genero"),
                created_at=result["created_at"],
            )
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            raise

    def get_user_by_email(self, email: str) -> Optional[dict]:
        query = "SELECT * FROM usuarios WHERE email = %s"
        return get_one(query, (email,))

    def get_user_by_id(self, user_id: int) -> Optional[dict]:
        query = "SELECT * FROM usuarios WHERE id = %s"
        return get_one(query, (user_id,))

    def update_user(
        self, user_id: int, user_data: UserUpdate
    ) -> Optional[UserResponse]:
        update_data = user_data.model_dump(exclude_unset=True)

        if not update_data:
            return self.get_user_by_id(user_id)

        # Mapear campos al español
        field_map = {
            "email": "email",
            "name": "nombre",
            "last_name": "apellido",
            "phone": "telefono",
            "date_of_birth": "fecha_nacimiento",
            "gender": "genero",
        }

        set_clause = []
        params = []
        for key, value in update_data.items():
            db_field = field_map.get(key, key)
            set_clause.append(f"{db_field} = %s")
            params.append(value)

        params.append(user_id)

        query = f"UPDATE usuarios SET {', '.join(set_clause)} WHERE id = %s RETURNING *"
        result = get_one(query, tuple(params))

        if result:
            return UserResponse(
                id=result["id"],
                email=result["email"],
                name=result["nombre"],
                last_name=result["apellido"],
                phone=result.get("telefono"),
                date_of_birth=str(result.get("fecha_nacimiento"))
                if result.get("fecha_nacimiento")
                else None,
                gender=result.get("genero"),
                created_at=result["created_at"],
            )
        return None

    def verify_password(self, email: str, password: str) -> Optional[UserResponse]:
        user = self.get_user_by_email(email)
        if user and user.get("password") == password:
            return UserResponse(
                id=user["id"],
                email=user["email"],
                name=user["nombre"],
                last_name=user["apellido"],
                phone=user.get("telefono"),
                date_of_birth=str(user.get("fecha_nacimiento"))
                if user.get("fecha_nacimiento")
                else None,
                gender=user.get("genero"),
                created_at=user["created_at"],
            )
        return None

    def store_reset_code(self, email: str, code: str):
        pass

    def verify_reset_code(self, email: str, code: str) -> bool:
        return False

    def reset_password(self, email: str, new_password: str) -> bool:
        query = "UPDATE usuarios SET password = %s WHERE email = %s"
        execute(query, (new_password, email))
        return True


user_repo = UserRepository()

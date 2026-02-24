from typing import Optional
from src.schemas.auth import UserUpdate, UserResponse
from src.repositories.user_repository import user_repo


class UserService:
    def get_current_user(self, user_id: int) -> Optional[UserResponse]:
        user = user_repo.get_user_by_id(user_id)
        if user:
            field_map = {
                "nombre": "name",
                "apellido": "last_name",
                "telefono": "phone",
                "fecha_nacimiento": "date_of_birth",
                "genero": "gender",
            }
            mapped = {}
            for k, v in user.items():
                if k != "password":
                    new_key = field_map.get(k, k)
                    if new_key == "date_of_birth" and v:
                        v = str(v)
                    mapped[new_key] = v
            return UserResponse(**mapped)
        return None

    def update_current_user(
        self, user_id: int, data: UserUpdate
    ) -> Optional[UserResponse]:
        return user_repo.update_user(user_id, data)


user_service = UserService()

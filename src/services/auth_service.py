import secrets
from src.schemas.auth import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
    ForgotPasswordRequest,
    ForgotPasswordResponse,
    VerifyResetCodeRequest,
    VerifyResetCodeResponse,
    ResetPasswordRequest,
    ResetPasswordResponse,
    LogoutResponse,
)
from src.repositories.user_repository import user_repo


class AuthService:
    def register(self, data: RegisterRequest) -> RegisterResponse:
        existing = user_repo.get_user_by_email(data.email)
        if existing:
            raise ValueError("El usuario ya existe")

        user = user_repo.create_user(data)
        return RegisterResponse(message="Usuario registrado exitosamente", user=user)

    def login(self, data: LoginRequest) -> LoginResponse:
        user = user_repo.verify_password(data.email, data.password)
        if not user:
            raise ValueError("Credenciales inválidas")

        token = secrets.token_urlsafe(32)
        return LoginResponse(access_token=token, user=user)

    def logout(self) -> LogoutResponse:
        return LogoutResponse(message="Sesión cerrada exitosamente")

    def forgot_password(self, data: ForgotPasswordRequest) -> ForgotPasswordResponse:
        user = user_repo.get_user_by_email(data.email)
        if not user:
            return ForgotPasswordResponse(
                message="Si el correo existe, recibirás un código de recuperación",
                reset_code=None,
            )

        code = secrets.token_hex(4).upper()
        user_repo.store_reset_code(data.email, code)
        return ForgotPasswordResponse(
            message="Código de recuperación enviado", reset_code=code
        )

    def verify_reset_code(
        self, data: VerifyResetCodeRequest
    ) -> VerifyResetCodeResponse:
        is_valid = user_repo.verify_reset_code(data.email, data.code)
        return VerifyResetCodeResponse(
            valid=is_valid, message="Código válido" if is_valid else "Código inválido"
        )

    def reset_password(self, data: ResetPasswordRequest) -> ResetPasswordResponse:
        success = user_repo.reset_password(data.email, data.new_password)
        if not success:
            raise ValueError("No se pudo restablecer la contraseña")
        return ResetPasswordResponse(message="Contraseña restablecida exitosamente")


auth_service = AuthService()

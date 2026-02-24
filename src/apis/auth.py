from fastapi import APIRouter, HTTPException, Header
from typing import Optional
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
    UserCreate,
    UserUpdate,
    UserResponse,
)
from src.services.auth_service import auth_service
from src.services.user_service import user_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=RegisterResponse)
def register(data: RegisterRequest):
    try:
        return auth_service.register(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    try:
        return auth_service.login(data)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.post("/logout", response_model=LogoutResponse)
def logout(authorization: Optional[str] = Header(None)):
    return auth_service.logout()


@router.post("/forgot-password", response_model=ForgotPasswordResponse)
def forgot_password(data: ForgotPasswordRequest):
    return auth_service.forgot_password(data)


@router.post("/verify-reset-code", response_model=VerifyResetCodeResponse)
def verify_reset_code(data: VerifyResetCodeRequest):
    return auth_service.verify_reset_code(data)


@router.post("/reset-password", response_model=ResetPasswordResponse)
def reset_password(data: ResetPasswordRequest):
    try:
        return auth_service.reset_password(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/me", response_model=UserResponse)
def get_current_user(x_user_id: int = Header(default=1)):
    user = user_service.get_current_user(x_user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@router.put("/me", response_model=UserResponse)
def update_current_user(data: UserUpdate, x_user_id: int = Header(default=1)):
    user = user_service.update_current_user(x_user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

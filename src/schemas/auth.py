from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    email: str
    name: str
    last_name: str
    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    date_of_birth: Optional[str] = None
    gender: Optional[str] = None


class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


class RegisterRequest(UserCreate):
    pass


class RegisterResponse(BaseModel):
    message: str
    user: UserResponse


class ForgotPasswordRequest(BaseModel):
    email: str


class ForgotPasswordResponse(BaseModel):
    message: str
    reset_code: Optional[str] = None


class VerifyResetCodeRequest(BaseModel):
    email: str
    code: str


class VerifyResetCodeResponse(BaseModel):
    valid: bool
    message: str


class ResetPasswordRequest(BaseModel):
    email: str
    new_password: str


class ResetPasswordResponse(BaseModel):
    message: str


class LogoutResponse(BaseModel):
    message: str

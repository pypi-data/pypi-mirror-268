from pydantic import (
    BaseModel,
)


class SignUpSchema(BaseModel):
    username: str
    telegram_id: int | None = None
    password: str | None = None


class LoginSchema(BaseModel):
    username: str
    password: str


class TMELoginSchema(BaseModel):
    telegram_id: int
    signature: str
    nonce: int
    timestamp: int


class RoleSchema(BaseModel):
    title: str


class UserSchema(BaseModel):
    username: str | None = None
    language: str | None = None


class ResetPasswordSchema(BaseModel):
    old_password: str
    new_password: str
    repeat_password: str

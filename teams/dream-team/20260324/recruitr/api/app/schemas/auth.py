from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    role: Literal["coach", "athlete"]

    # optional coach-only fields for quick demo setup
    first_name: str | None = None
    last_name: str | None = None
    title: str | None = None
    organization_name: str | None = None
    sport: str | None = None
    level: str | None = None
    bio: str | None = None


class LoginRequest(BaseModel):
    # Keep login tolerant to avoid 422 for minor client-side input issues.
    email: str = ""
    password: str = ""


class DevLoginRequest(BaseModel):
    role: Literal["coach", "athlete"]


class MeResponse(BaseModel):
    id: int
    email: str
    roles: list[str]
    primary_role: str | None = None
    coach_profile: dict | None = None
    athlete_profile: dict | None = None


class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: MeResponse

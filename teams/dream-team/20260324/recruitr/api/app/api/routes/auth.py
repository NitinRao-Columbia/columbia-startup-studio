from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)
from app.db.deps import get_db
from app.models.coach_profile import CoachProfile
from app.models.role import Role
from app.models.user import User
from app.models.user_roles import UserRole
from app.schemas.auth import AuthResponse, DevLoginRequest, LoginRequest, MeResponse, RegisterRequest

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])
bearer_scheme = HTTPBearer()


def _get_user_roles(db: Session, user_id: int) -> list[str]:
    rows = db.execute(
        select(Role.key)
        .join(UserRole, UserRole.role_id == Role.id)
        .where(UserRole.user_id == user_id)
    ).all()
    return [row[0] for row in rows]


def _get_coach_profile_dict(db: Session, user_id: int) -> dict | None:
    cp = db.execute(
        select(CoachProfile).where(CoachProfile.user_id == user_id)
    ).scalar_one_or_none()

    if not cp:
        return None

    school_name = None
    if cp.school_unitid:
        school_name = db.execute(
            text("SELECT name FROM public.schools WHERE unitid = :unitid"),
            {"unitid": cp.school_unitid},
        ).scalar()

    return {
        "id": cp.id,
        "first_name": cp.first_name,
        "last_name": cp.last_name,
        "title": cp.title,
        "organization_name": cp.organization_name,
        "school_unitid": cp.school_unitid,
        "school_name": school_name,
        "sport": cp.sport,
        "level": cp.level,
        "bio": cp.bio,
        "is_verified_coach": cp.is_verified_coach,
    }


def _get_athlete_profile_dict(db: Session, user_id: int) -> dict | None:
    row = db.execute(
        text(
            """
            SELECT
              ap.user_id,
              ap.first_name,
              ap.last_name,
              ap.sport,
              ap.grad_year,
              ap.positions,
              ap.state,
              ap.country,
              ap.willing_to_travel,
              ap.travel_radius_mi,
              ap.club_team,
              ap.school_unitid,
              s.name AS school_name,
              ap.high_school,
              ap.bio
            FROM public.athlete_profiles ap
            LEFT JOIN public.schools s
              ON s.unitid = ap.school_unitid
            WHERE ap.user_id = :user_id
            """
        ),
        {"user_id": user_id},
    ).mappings().first()
    if not row:
        return None

    return {
        "user_id": int(row["user_id"]),
        "first_name": row["first_name"],
        "last_name": row["last_name"],
        "sport": row["sport"],
        "grad_year": row["grad_year"],
        "positions": row["positions"] or [],
        "state": row["state"],
        "country": row["country"],
        "willing_to_travel": (
            bool(row["willing_to_travel"]) if row["willing_to_travel"] is not None else None
        ),
        "travel_radius_mi": row["travel_radius_mi"],
        "club_team": row["club_team"],
        "school_unitid": row["school_unitid"],
        "school_name": row["school_name"],
        "high_school": row["high_school"],
        "bio": row["bio"],
    }


def _build_me_response(db: Session, user: User) -> MeResponse:
    roles = _get_user_roles(db, user.id)
    primary_role = roles[0] if roles else None

    return MeResponse(
        id=user.id,
        email=user.email,
        roles=roles,
        primary_role=primary_role,
        coach_profile=_get_coach_profile_dict(db, user.id) if "coach" in roles else None,
        athlete_profile=_get_athlete_profile_dict(db, user.id) if "athlete" in roles else None,
    )


def _get_or_create_role(db: Session, role_key: str) -> Role:
    role = db.execute(select(Role).where(Role.key == role_key)).scalar_one_or_none()
    if role:
        return role

    # safety for local dev if roles weren't seeded
    role = Role(key=role_key, name=role_key.capitalize())
    db.add(role)
    db.flush()
    return role


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    payload = decode_access_token(token)

    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    try:
        user_id = int(payload["sub"])
    except (TypeError, ValueError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token subject",
        )

    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    return user


@router.post("/register", response_model=AuthResponse)
def register(payload: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.execute(select(User).where(User.email == payload.email)).scalar_one_or_none()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    role = _get_or_create_role(db, payload.role)

    user = User(
        email=str(payload.email).lower(),
        password_hash=hash_password(payload.password),
        is_active=True,
        is_email_verified=True,  # dev-friendly for now
    )
    db.add(user)
    db.flush()  # get user.id

    db.add(UserRole(user_id=user.id, role_id=role.id))

    if payload.role == "coach":
        db.add(
            CoachProfile(
                user_id=user.id,
                first_name=payload.first_name or "Demo",
                last_name=payload.last_name or "Coach",
                title=payload.title,
                organization_name=payload.organization_name,
                sport=payload.sport,
                level=payload.level,
                bio=payload.bio,
                is_verified_coach=False,
            )
        )

    db.commit()
    db.refresh(user)

    token = create_access_token({"sub": str(user.id)})
    return AuthResponse(access_token=token, user=_build_me_response(db, user))


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    email = (payload.email or "").strip().lower()
    password = payload.password or ""

    if not email:
        raise HTTPException(status_code=400, detail="Email is required")
    if "@" not in email:
        raise HTTPException(status_code=400, detail="Enter a valid email address")
    if not password:
        raise HTTPException(status_code=400, detail="Password is required")

    user = db.execute(
        select(User).where(User.email == email)
    ).scalar_one_or_none()

    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_access_token({"sub": str(user.id)})
    return AuthResponse(access_token=token, user=_build_me_response(db, user))


@router.post("/dev-login", response_model=AuthResponse)
def dev_login(payload: DevLoginRequest, db: Session = Depends(get_db)):
    """
    Fast shortcut for UI demos: creates (if missing) and logs in a coach/athlete demo account.
    """
    email = f"demo.{payload.role}@example.com"
    password = "demo1234"

    user = db.execute(select(User).where(User.email == email)).scalar_one_or_none()

    if not user:
        role = _get_or_create_role(db, payload.role)

        user = User(
            email=email,
            password_hash=hash_password(password),
            is_active=True,
            is_email_verified=True,
        )
        db.add(user)
        db.flush()

        db.add(UserRole(user_id=user.id, role_id=role.id))

        if payload.role == "coach":
            db.add(
                CoachProfile(
                    user_id=user.id,
                    first_name="Cam",
                    last_name="Wilson",
                    title="Assistant Coach",
                    organization_name="Columbia University",
                    sport="Soccer",
                    level="D1",
                    bio="Demo coach account for Recruitr UI testing.",
                    is_verified_coach=False,
                )
            )

        db.commit()
        db.refresh(user)

    token = create_access_token({"sub": str(user.id)})
    return AuthResponse(access_token=token, user=_build_me_response(db, user))


@router.get("/me", response_model=MeResponse)
def me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return _build_me_response(db, current_user)

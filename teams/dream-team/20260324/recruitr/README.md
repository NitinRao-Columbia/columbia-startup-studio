# Recruitr — Backend API (FastAPI) 🚀

Recruitr is a sports recruiting platform (coach-first + athlete-facing) being built as a web/mobile product concept.

This repository contains the **backend API** for Recruitr, including:
- FastAPI app
- PostgreSQL database
- SQLAlchemy ORM models
- Alembic migrations
- Initial auth/domain schema (users, roles, coach profiles)

---

## Project Status (Current)

### ✅ Working now
- FastAPI app runs locally
- `/health` endpoint works
- Swagger docs (`/docs`) work
- PostgreSQL local dev database is installed and running
- Alembic migrations are configured and working
- Initial schema migrated successfully:
  - `users`
  - `roles`
  - `user_roles`
  - `coach_profiles`
- Manual seed + join smoke test passed (user + role + coach profile linked correctly)

### 🚧 In progress / next
- Auth endpoints (register/login)
- Password hashing utility
- SQLAlchemy session dependency (`get_db`)
- Pydantic request/response schemas
- Role seeding script (Python)
- Tests (unit + integration)
- Athlete profile schema and endpoints
- Media uploads (MinIO/S3)
- Realtime/messaging integration

---

## What We’ve Built / Done So Far (Milestone Recap)

### 1) Python environment setup
- Created and used local virtual environment (`.venv`)
- Verified project Python and Uvicorn paths point to `.venv`
- Upgraded runtime to **Python 3.12** (required for modern typing like `str | None`)

### 2) Fixed backend startup/import issues
- Resolved `ModuleNotFoundError` for `app.core.config`
- Confirmed package structure (`app/`, `core/`, `__init__.py`) and correct run path from project root
- Verified app starts with Uvicorn

### 3) Fixed Python typing compatibility issue
- Hit SQLAlchemy model typing error:
  - `TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'`
- Root cause: Python 3.9 incompatible with `X | None` union typing
- Fix: upgrade to Python 3.12

### 4) Debugged settings / env config issues
- Found malformed `DATABASE_URL` parsing issue (env formatting problem)
- Found Pydantic settings validation errors (missing required keys + extra legacy keys)
- Cleaned/aligned env vars with current `Settings` model expectations

### 5) Installed PostgreSQL locally and configured dev DB
- Installed full PostgreSQL locally (Homebrew)
- Installed `psql`
- Created local dev role + database:
  - DB: `recruitr`
  - User: `recruitr`
- Verified connection with `psql`

### 6) Alembic migrations working
- Ran autogenerate for initial schema
- Created migration:
  - `bd04ab0d0138_create_users_roles_coach_profiles.py`
- Applied migration with `alembic upgrade head`
- Confirmed `alembic_version` table state

### 7) Manual DB smoke test
- Inserted roles (`coach`, `athlete`, `admin`)
- Inserted test user
- Linked user to `coach` role in `user_roles`
- Inserted `coach_profiles` record
- Verified joins across all tables

---

## Tech Stack (Current + Planned)

## Backend (current)
- **Python 3.12**
- **FastAPI**
- **Uvicorn** (ASGI server, reload in dev)
- **SQLAlchemy 2.x** (ORM)
- **Alembic** (migrations)
- **PostgreSQL 16** (local dev DB)
- **psycopg** (Postgres driver)
- **Pydantic v2 / pydantic-settings** (config/settings)

## Dev tools (current)
- **venv** (Python virtual environment)
- **Homebrew** (Postgres install on macOS)
- **psql** (Postgres CLI)

## Likely/Planned backend dependencies (based on project direction)
- **Passlib / bcrypt** (password hashing)
- **python-jose / PyJWT** (JWT auth)
- **pytest** (testing)
- **httpx** (API tests)
- **MinIO / S3 client** (media storage)
- **Centrifugo** (realtime messaging / notifications, planned)

## Product / platform direction (higher-level)
- Web app + mobile app concept for sports recruiting
- Coach + athlete accounts
- Media uploads (highlight reels, profiles)
- Messaging / notifications
- Search/discovery workflows
- Role-based access

> Note: Some env vars in your config indicate **MinIO/S3** and **realtime secrets** are expected soon, even if those services are not fully wired yet.

---

## Current Backend Schema (v1)

Tables created:
- `users`
- `roles`
- `user_roles`
- `coach_profiles`
- `alembic_version`

See schema diagram:
- `docs/db_schema.mmd` (Mermaid ER diagram)

### Key design notes
- `users.email` is unique
- `coach_profiles.user_id` is unique (1 coach profile per user)
- `user_roles` is a join table with composite PK (`user_id`, `role_id`)
- Foreign keys use `ON DELETE CASCADE`

---

## Repository Layout (Current / Expected)

> Adjust if your actual tree differs slightly.

```text
api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── role.py
│   │   ├── user_role.py
│   │   └── coach_profile.py
│   └── ... (future: api/routes, schemas, services, db session, auth)
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
│       └── bd04ab0d0138_create_users_roles_coach_profiles.py
├── alembic.ini
├── .env                # local dev env (not committed)
├── .venv/              # local venv (not committed)
└── README.md


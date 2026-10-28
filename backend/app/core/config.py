from pathlib import Path
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict

# backend/app/core/config.py -> BACKEND_DIR là parents[2], REPO_ROOT là parents[3]
BACKEND_DIR = Path(__file__).resolve().parents[2]
REPO_ROOT = BACKEND_DIR.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        case_sensitive=True,
        extra="ignore",
    )

    PROJECT_NAME: str = "NEU Career AI API"
    API_V1_STR: str = "/api"
    ENVIRONMENT: str = "development"

    # Gemini
    GEMINI_API_KEY: str = ""
    GEMINI_MODEL: str = "gemini-2.5-flash"

    # Database
    DATABASE_URL: str = f"sqlite:///{(BACKEND_DIR / 'neu_career.db').as_posix()}"

    # Upload CV
    MAX_UPLOAD_MB: int = 5

    # Thư mục chứa prompt template do nhóm AI quản lý (ai/prompts)
    PROMPTS_DIR: Path = REPO_ROOT / "ai" / "prompts"

    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
    ]


settings = Settings()

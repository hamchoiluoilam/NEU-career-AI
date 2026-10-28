from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings

_connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(settings.DATABASE_URL, connect_args=_connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def init_db() -> None:
    """Tạo bảng nếu chưa có. Gọi một lần khi khởi động app."""
    from app import models  # noqa: F401  (đăng ký model vào Base.metadata)

    Base.metadata.create_all(bind=engine)


def get_db():
    """Dependency cung cấp session CSDL cho từng request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

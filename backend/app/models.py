from datetime import datetime, timezone
from typing import Any, List

from sqlalchemy import JSON, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class InterviewSession(Base):
    __tablename__ = "interview_sessions"

    id: Mapped[str] = mapped_column(String(32), primary_key=True)
    candidate_name: Mapped[str] = mapped_column(String(255))
    target_role: Mapped[str] = mapped_column(String(255))
    turn_index: Mapped[int] = mapped_column(Integer, default=1)
    is_finished: Mapped[bool] = mapped_column(default=False)
    # Danh sách {"role": "assistant|user", "content": str}
    history: Mapped[List[Any]] = mapped_column(JSON, default=list)
    # Danh sách điểm STAR của từng câu trả lời
    evaluations: Mapped[List[Any]] = mapped_column(JSON, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_utcnow)

from datetime import datetime
from sqlalchemy import String, Text, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base


class World(Base):
    __tablename__ = "worlds"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

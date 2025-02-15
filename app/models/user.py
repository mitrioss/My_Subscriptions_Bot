from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer

from app.database import Base
from app.models.user_subscription import UserSubscription

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        description="Уникальный идентификатор пользователя")

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        description="Уникальное имя пользователя")

    subscriptions: Mapped[List["UserSubscription"]] = relationship(
        "UserSubscription",
    back_populates="user")

    def __str__(self):
        # Возвращает строку с username
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"name={self.self.username!r})")


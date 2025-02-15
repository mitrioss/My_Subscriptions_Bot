from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Integer

from app.database import Base
from app.models.subscription import Subscription
from app.models.user import User


class UserSubscription(Base):
    __tablename__ = "user_subscriptions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        description="Уникальный идентификатор записи")

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        description="ID пользователя, который оформил подписку")

    subscription_id: Mapped[int] = mapped_column(
        ForeignKey("subscriptions.id"),
        nullable=False,
        description="ID подписки")

    cost: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        description="Стоимость подписки")

    next_payment_date: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False,
        description="Дата следующего платежа")

    comment: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
        description="Комментарий пользователя к подписке")

    user: Mapped["User"] = relationship(
        "User",
        back_populates="subscriptions")
    subscription: Mapped["Subscription"] = relationship(
        "Subscription",
        back_populates="user_subscriptions")

    def __str__(self):
        # Возвращает строку с id подписки и названием подписки
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"subscription_name={self.subscription.name!r})")
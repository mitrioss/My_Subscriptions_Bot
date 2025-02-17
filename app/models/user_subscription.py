'''from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Integer

from app.database import Base


class UserSubscription(Base):
    __tablename__ = "user_subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False, ondelete="CASCADE")

    subscription_id: Mapped[int] = mapped_column(
        ForeignKey("subscriptions.id"), nullable=False)

    cost: Mapped[int] = mapped_column(
        Integer, nullable=False,)

    next_payment_date: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False)

    comment: Mapped[str] = mapped_column(
        String(255), nullable=True)

    user: Mapped["User"] = relationship(
        "User", back_populates="subscriptions"
    )  # Строковая аннотация для "User"

    subscription: Mapped["Subscription"] = relationship(
        "Subscription", back_populates="user_subscriptions"
    )

    def __str__(self):
        # Возвращает строку с id подписки и названием подписки
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"subscription_name={self.subscription.name!r})")
'''
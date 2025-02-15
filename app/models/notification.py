from sqlalchemy import Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.database import Base
from app.models.user_subscription import UserSubscription


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
        description="Уникальный идентификатор уведомления"
    )

    user_subscription_id: Mapped[int] = mapped_column(
        ForeignKey("user_subscriptions.id"),
        nullable=False,
        description="ID подписки, по которой отправляется уведомление"
    )

    notify_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False,
        description="Дата уведомления"
    )

    is_sent: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
        description="Статус отправки уведомления (True - отправлено, False - не отправлено)"
    )

    user_subscription: Mapped["UserSubscription"] = relationship(
        "UserSubscription", back_populates="notifications"
    )

    def __str__(self):
        # Возвращает строку с username
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"subscription_name={self.user_subscription_id!r})")

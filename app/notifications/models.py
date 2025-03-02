from sqlalchemy import Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(primary_key=True,)

    subscription_id: Mapped[int] = mapped_column(
        ForeignKey("subscriptions.id"), nullable=False)

    notify_date: Mapped[Date] = mapped_column(
        Date, nullable=False)

    is_sent: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False)

    subscription: Mapped["UserSubscription"] = relationship(
        "Subscription", back_populates="notifications"
    )

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, subscription_id={self.subscription_id!r})"

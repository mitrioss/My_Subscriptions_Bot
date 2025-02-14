from sqlalchemy import Column, Integer, ForeignKey, Date, Boolean
from sqlalchemy.orm import relationship
from app.database.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    user_subscription_id = Column(Integer,
                                  ForeignKey('user_subscriptions.id'),
                                  nullable=False)
    notify_date = Column(Date, nullable=False)
    status = Column(Boolean, default=False)  # False - не отправлено, True - отправлено

    user_subscription = relationship("UserSubscription",
                                     back_populates="notifications")

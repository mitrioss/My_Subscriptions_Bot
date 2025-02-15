from enum import Enum
from sqlalchemy import String, Integer
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.user_subscription import UserSubscription


class Category(str, Enum):
    STREAMING = "Стриминговые сервисы"
    MUSIC = "Музыкальные сервисы"
    GAMING = "Игровые подписки"
    BOOKS = "Книги и аудиокниги"
    EDUCATION = "Образование"
    SOFTWARE = "Программы и инструменты"
    FINANCE = "Финансовые сервисы"
    BUSINESS = "Бизнес-сервисы"
    HEALTH = "Здоровье и фитнес"
    FOOD = "Доставка еды"
    TRANSPORT = "Транспорт"
    VPN = "VPN и безопасность"
    CLOUD = "Облачные сервисы"

class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        description="Уникальный идентификатор подписки")

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        description="Название подписки")

    category: Mapped[Category] = mapped_column(
        Enum(Category),
        nullable=False,
        index=True,
        description="Категория подписки")

    user_subscriptions: Mapped[list["UserSubscription"]] = relationship(
        "UserSubscription", back_populates="subscription")


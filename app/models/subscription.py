from enum import Enum
from sqlalchemy import String, Integer, Enum as SQLAlchemyEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


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

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False)

    category: Mapped[Category] = mapped_column(
        SQLAlchemyEnum(Category), nullable=False, index=True)

    user_subscriptions: Mapped[list["UserSubscription"]] = relationship(
        "UserSubscription", back_populates="subscription")

    def __str__(self):
        # Возвращает строку с username
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"subscription_name={self.name!r})")

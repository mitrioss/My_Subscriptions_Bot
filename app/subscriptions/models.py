from enum import Enum
from sqlalchemy import String, ForeignKey, DateTime, Integer, Enum as SQLAlchemyEnum
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
    __tablename__ = "user_subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(50), nullable=False)

    category: Mapped[Category] = mapped_column(
        SQLAlchemyEnum(Category), nullable=False, index=True)

    cost: Mapped[int] = mapped_column(
        Integer, nullable=False,)

    next_payment_date: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False)

    comment: Mapped[str] = mapped_column(
        String(50), nullable=True)

    user: Mapped["User"] = relationship(
        "User", back_populates="subscriptions"
    )  # Строковая аннотация для "User"


    def __str__(self):
        # Возвращает строку с username
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"subscription_name={self.name!r})")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "category": self.category,
            "cost": self.cost,
            "next_payment_date": self.next_payment_date,
            "comment": self.comment
        }
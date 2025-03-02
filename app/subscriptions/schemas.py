from enum import Enum
from pydantic import BaseModel, Field, ConfigDict, validator
from datetime import date, datetime


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


class SSubscription(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    name: str = Field(..., min_length=1, max_length=50, description="Название подписки, от 1 до 50 символов")
    category: Category = Field(..., description='Категория подписки')
    cost: int = Field(..., ge=1, le=10_000, description="Цена подписки, от 1 до 10 000 рублей")
    next_payment_date: date = Field(..., description="Дата списания подписки")
    comment: str = Field(..., min_length=1, max_length=50, description="Описание подписки, от 1 до 50 символов")

    @validator("next_payment_date", pre=True)
    def validate_next_payment_date(cls, value):
        """ Убираем время, оставляем только дату """
        if isinstance(value, str):
            value = date.fromisoformat(value.split("T")[0])  # Берём только YYYY-MM-DD
        elif isinstance(value, datetime):
            value = value.date()  # Преобразуем datetime в date

        if value < date.today():
            raise ValueError("Дата следующего списания не может быть в прошлом")
        return value

class SSubscriptionAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    name: str = Field(..., min_length=1, max_length=50, description="Название подписки, от 1 до 50 символов")
    category: Category = Field(..., description='Категория подписки')
    cost: int = Field(..., ge=1, le=10_000, description="Цена подписки, от 1 до 10 000 рублей")
    next_payment_date: date = Field(..., description="Дата списания подписки")
    comment: str = Field(..., min_length=1, max_length=50, description="Описание подписки, от 1 до 50 символов")

    @validator("category", pre=True)
    def validate_category(cls, value):
        """ Преобразует английский `STREAMING` в русское значение Enum """
        if isinstance(value, str) and value in Category.__members__:
            return Category[value]
        return value

    @validator("next_payment_date", pre=True)
    def validate_next_payment_date(cls, value):
        """ Убираем время, оставляем только дату """
        if isinstance(value, str):
            value = date.fromisoformat(value.split("T")[0])  # Берём только YYYY-MM-DD
        if value < date.today():
            raise ValueError("Дата следующего списания не может быть в прошлом")
        return value
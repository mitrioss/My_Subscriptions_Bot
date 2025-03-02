from datetime import datetime
from enum import Enum


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


class RBSubscription:
    def __init__(self, sub_id: int | None = None,
                 user_id: int | None = None,
                 name: str | None = None,
                 category: Category | None = None,
                 cost: int | None = None,
                 next_payment_date: datetime | None = None,
                 comment: str | None = None
                 ):
        self.id = sub_id
        self.user_id = user_id
        self.name = name
        self.category = category
        self.cost = cost
        self.next_payment_date = next_payment_date
        self.comment = comment


    def to_dict(self) -> dict:
        data = {'id': self.id,'user_id': self.user_id, 'name': self.name, 'category': self.category,
                'cost': self.cost, 'next_payment_date': self.next_payment_date,
                'comment': self.comment}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
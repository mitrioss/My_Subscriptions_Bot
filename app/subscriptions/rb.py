from enum import Enum


class RBSubscription:
    def __init__(self, sub_id: int | None = None,
                 name: str | None = None,
                 category: Enum | None = None):
        self.id = sub_id
        self.name = name
        self.category = category


    def to_dict(self) -> dict:
        data = {'id': self.id, 'name': self.name, 'category': self.category}
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data
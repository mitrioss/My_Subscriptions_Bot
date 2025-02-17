from enum import Enum
from pydantic import BaseModel, Field, ConfigDict



class SSubscription(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(..., min_length=1, max_length=50, description="Название подписки, от 1 до 50 символов")
    category: Enum = Field(..., description='Категория подписки')


class SSubscriptionAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    name: str = Field(..., min_length=1, max_length=50, description="Название подписки, от 1 до 50 символов")
    category: Enum = Field(..., description='Категория подписки')
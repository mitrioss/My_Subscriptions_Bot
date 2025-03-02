from pydantic import BaseModel, Field, ConfigDict


class SUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str = Field(..., min_length=1, max_length=50, description="Имя пользователя, от 1 до 50 символов")


class SUserAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    username: str = Field(..., min_length=1, max_length=50, description="Имя пользователя, от 1 до 50 символов")
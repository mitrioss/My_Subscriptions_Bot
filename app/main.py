from fastapi import FastAPI
from app.api import users
from app.database import engine
from app.database.base import Base


# Создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключаем роутеры
app.include_router(users.router)

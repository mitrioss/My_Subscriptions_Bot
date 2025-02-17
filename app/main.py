from fastapi import FastAPI
from app.database import engine, Base
from app.users.router import router as router_users
from app.subscriptions.router import router as router_sub


# Создаем таблицы
#Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


app.include_router(router_users)
app.include_router(router_sub)

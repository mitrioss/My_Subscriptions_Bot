from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse


# создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()


# определяем зависимость
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return FileResponse("../public/index.html")


@app.get("/api/users")
def get_user(db: Session = Depends(get_db)):
    return db.query(User).all()


@app.get("/api/users/{id}")
def get_user(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    user = db.query(User).filter(User.id == id).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if user == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, отправляем его
    return user


@app.post("/api/users")
def create_user(data=Body(), db: Session = Depends(get_db)):
    user = User(name=data["name"])
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.put("/api/users")
def edit_user(data=Body(), db: Session = Depends(get_db)):
    # получаем пользователя по id
    user = db.query(User).filter(User.id == data["id"]).first()
    # если не найден, отправляем статусный код и сообщение об ошибке
    if user == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    # если пользователь найден, изменяем его данные и отправляем обратно клиенту
    user.name = data["name"]
    db.commit()  # сохраняем изменения 
    db.refresh(user)
    return user


@app.delete("/api/users/{id}")
def delete_user(id, db: Session = Depends(get_db)):
    # получаем пользователя по id
    user = db.query(User).filter(User.id == id).first()

    # если не найден, отправляем статусный код и сообщение об ошибке
    if user == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})

    # если пользователь найден, удаляем его
    db.delete(user)  # удаляем объект
    db.commit()  # сохраняем изменения
    return user



from fastapi import FastAPI
from app.api import users
from app.database.session import engine
from app.database.base import Base

# Создаем таблицы
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Подключаем роутеры
app.include_router(users.router)

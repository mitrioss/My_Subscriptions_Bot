from fastapi import APIRouter, Depends
from app.users.dao import UserDAO
from app.users.rb import RBUser
from app.users.schemas import SUser, SUserAdd
from app.users.schemas import SUserAdd

router = APIRouter(prefix='/users', tags=['Работа с пользователями'])

@router.get("/", summary="Получить всех пользователей")
async def get_all_user(request_body: RBUser = Depends()) -> list[SUser]:
    return await UserDAO.find_all(**request_body.to_dict())

@router.get("/{user_id}", summary="Получить пользователя по id")
async def get_user_by_id(user_id: int) -> SUser | dict:
    rez = await UserDAO.find_one_or_none_by_id(user_id)
    if rez is None:
        return {'message': f'Пользователь с ID {user_id} не найден!'}
    return rez

@router.post("/add/", summary="Создать нового пользователя")
async def register_user(user: SUserAdd) -> dict:
    check = await UserDAO.add(**user.dict())
    if check:
        return {"message": "Пользователь успешно создан!", "user": user}
    else:
        return {"message": "Ошибка при создании пользователя!"}
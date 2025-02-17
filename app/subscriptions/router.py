from fastapi import APIRouter, Depends
from app.subscriptions.dao import SubscriptionDAO
from app.subscriptions.rb import RBSubscription
from app.subscriptions.schemas import SSubscription, SSubscriptionAdd


router = APIRouter(prefix='/sub', tags=['Работа с подписками'])

@router.get("/", summary="Получить все подписки")
async def get_all_user(request_body: RBSubscription = Depends()) -> list[SSubscription]:
    return await SubscriptionDAO.find_all(**request_body.to_dict())

@router.get("/{user_id}", summary="Получить подписку по id")
async def get_user_by_id(user_id: int) -> SSubscription | dict:
    rez = await SubscriptionDAO.find_one_or_none_by_id(user_id)
    if rez is None:
        return {'message': f'Подписка с ID {user_id} не найдена!'}
    return rez

@router.post("/add/", summary="Создать новую подписку")
async def register_user(user: SSubscriptionAdd) -> dict:
    check = await SubscriptionDAO.add(**user.dict())
    if check:
        return {"message": "Подписка успешно создана!", "user": user}
    return {"message": "Ошибка при создании подписки!"}
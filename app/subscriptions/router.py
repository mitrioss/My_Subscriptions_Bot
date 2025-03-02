from fastapi import APIRouter, Depends
from app.subscriptions.dao import SubscriptionDAO
from app.subscriptions.rb import RBSubscription
from app.subscriptions.schemas import SSubscription, SSubscriptionAdd


router = APIRouter(prefix='/sub', tags=['Работа с подписками'])

@router.get("/", summary="Получить все подписки")
async def get_all_sub(request_body: RBSubscription = Depends()) -> list[SSubscription]:
    return await SubscriptionDAO.find_all(**request_body.to_dict())

@router.get("/{sub_id}", summary="Получить подписку по id")
async def get_sub_by_id(sub_id: int) -> SSubscription | dict:
    rez = await SubscriptionDAO.find_one_or_none_by_id(sub_id)
    if rez is None:
        return {'message': f'Подписка с ID {sub_id} не найдена!'}
    return rez

@router.get("/by_filter", summary="Получить одну подписку по фильтру")
async def get_student_by_filter(request_body: RBSubscription = Depends()) -> SSubscription | dict:
    rez = await SubscriptionDAO.find_one_or_none(**request_body.to_dict())
    if rez is None:
        return {'message': f'Подписка с указанными вами параметрами не найдена!'}
    return rez

@router.post("/add/", summary="Создать новую подписку")
async def add_sub(subscription: SSubscriptionAdd) -> dict:
    check = await SubscriptionDAO.add(**subscription.dict())
    if check:
        return {"message": "Подписка успешно создана!", "subscription": subscription}
    return {"message": "Ошибка при создании подписки!"}
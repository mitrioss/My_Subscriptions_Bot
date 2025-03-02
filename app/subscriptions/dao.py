from sqlalchemy import insert, update, delete
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from app.dao.base import BaseDAO
from app.users.models import User
from app.subscriptions.models import Subscription
from app.database import async_session_maker


class SubscriptionDAO(BaseDAO):
    model = Subscription

    @classmethod
    async def find_full_data(cls, student_id: int):
        async with async_session_maker() as session:
            # Запрос для получения информации о студенте вместе с информацией о факультете
            query = select(cls.model).options(joinedload(cls.model.user)).filter_by(id=student_id)
            result = await session.execute(query)
            subscription_info = result.scalar_one_or_none()

            # Если студент не найден, возвращаем None
            if not subscription_info:
                return None

            subscription_data = subscription_info.to_dict()
            subscription_data['subscription'] = subscription_info.user.username
            return subscription_data
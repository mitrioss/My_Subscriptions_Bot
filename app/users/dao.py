from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.subscriptions.models import Subscription
from app.users.models import User
from sqlalchemy.future import select

class UserDAO(BaseDAO):
    model = User

from fastapi import HTTPException
from passlib.context import CryptContext
from asyncpg import UniqueViolationError
from starlette.requests import Request

from db import database
from managers.auth import AuthManager
from models import users, RoleType
from schemas.request.user import UserChangeData
from schemas.response.user import UserOut

# isntancia para hashear contraseñas o algo
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserManager:
    # registra un usuario en la base de datos
    @staticmethod
    async def register(user_data):
        user_data["password"] = pwd_context.hash(user_data["password"])
        try:
            id_ = await database.execute(users.insert().values(**user_data))
        except UniqueViolationError:
            raise HTTPException(400, "User with this email already exists")
        user_do = await database.fetch_one(users.select().where(users.c.id == id_))
        return AuthManager.encode_token(user_do)

    @staticmethod
    async def login(user_data):
        user_do = await database.fetch_one(users.select().where(users.c.email == user_data["email"]))
        if not user_do:
            raise HTTPException(400, "Wrong email or password")
        # la funcion verify verifica las contraseñas de los datos actuales ingesados con los de la db
        elif not pwd_context.verify(user_data["password"], user_do["password"]):
            raise HTTPException(400, "Wrong email or password")
        return AuthManager.encode_token(user_do)

    @staticmethod
    async def get_all_users():
        return await database.fetch_all(users.select())

    @staticmethod
    async def chanche_user_data(user_data: dict, request: Request):
        current_user = AuthManager.get_current_user(request)
        user_data["id"] = current_user.id
        await database.execute(users.update().where(users.c.id == current_user.id).values(**user_data))
        updated_user = await database.fetch_one(users.select().where(users.c.id == current_user.id))
        return UserOut(**updated_user)

    @staticmethod
    async def get_user_by_email(email):
        return await database.fetch_all(users.select().where(users.c.email == email))

    @staticmethod
    async def change_role(role: RoleType, user_id):
        await database.execute(users.update().where(users.c.id == user_id).values(role=role))

    @staticmethod
    async def delete(user_id):
        await database.execute(users.delete().where(users.c.id == user_id))
from datetime import datetime, timedelta
from typing import Optional

import jwt
from decouple import config
from fastapi import HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.requests import Request

from db import database
from models import users, RoleType


class AuthManager:

    @staticmethod
    def encode_token(user):
        try:
            payload = {
                "sub": user["id"],
                "exp": datetime.utcnow() + timedelta(minutes=120)

            }
            return jwt.encode(payload, config('SECRET_KEY'), algorithm="HS256")
        except Exception as ex:
            raise ex

    @staticmethod
    def get_current_user(request: Request):
        user = request.state.user
        if not user:
            raise HTTPException(403, "Forbidden")
        return user

class CustomHTTPBearer(HTTPBearer):
    async def __call__(
            # Request(importar starlette)
            self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        # el super esta en la clase HTTPBearer para ver como funciona
        res = await super().__call__(request)

        try:
            payload = jwt.decode(
                res.credentials, config("SECRET_KEY"), algorithms=["HS256"]
            )
            user_data = await database.fetch_one(
                users.select().where(users.c.id == payload["sub"])
            )
            request.state.user = user_data
            return user_data
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, "Token is expired")
        except jwt.InvalidTokenError:
            raise HTTPException(401, "Invalid token")


# para proteger las rutas con la autenticacion
oauth2_scheme = CustomHTTPBearer()


def is_base(request: Request):
    if not request.state.user["Rol"] == RoleType.base:
        raise HTTPException(403, "Forbidden")


def is_admin(request: Request):
    if not request.state.user["Rol"] == RoleType.admin:
        raise HTTPException(403, "Forbidden")


from typing import Optional, List

from fastapi import APIRouter, Depends
from starlette.requests import Request

from managers.auth import oauth2_scheme, is_admin, AuthManager
from managers.users import UserManager
from models import RoleType
from schemas.response.user import UserOut
from schemas.request.user import UserChangeData

router = APIRouter(tags=["Users"])


@router.get("/users/", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], response_model=List[UserOut])
async def get_users(email: Optional[str] = None):
    if email:
        return await UserManager.get_user_by_email(email)

    return await UserManager.get_all_users()


@router.put("/users/{users_id}/editar_datos",
            dependencies=[Depends(oauth2_scheme), Depends(AuthManager.get_current_user)], response_model=UserOut)
async def cambiar_datos_user(user_data: UserChangeData, request: Request):
    return await UserManager.chanche_user_data(user_data.dict(), request)


@router.delete("/users/{users_id}/", dependencies=[Depends(oauth2_scheme), Depends(is_admin)],
               status_code=204)  # 204 exito no retorna nada
async def delete_user(user_id: int):
    await UserManager.delete(user_id)


# put porque es un update
@router.put("/users/{users_id}/make-admin", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def make_admin(user_id: int):
    await UserManager.change_role(RoleType.admin, user_id)


# put porque es un update
@router.put("/users/{users_id}/make-base", dependencies=[Depends(oauth2_scheme), Depends(is_admin)], status_code=204)
async def make_base(user_id: int):
    await UserManager.change_role(RoleType.base, user_id)

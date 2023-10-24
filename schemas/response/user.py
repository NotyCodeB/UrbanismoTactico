from models import RoleType
from schemas.base import UserBase


class UserOut(UserBase):
    id: int
    nombre: str
    telefono: str
    Rol: RoleType
    direccion: str
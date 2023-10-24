from schemas.base import UserBase


class UserRegisterIn(UserBase):
    nombre: str
    password: str
    telefono: str
    direccion: str

class UserChangeData(UserBase):
    nombre: str
    telefono: str
    direccion: str


class UserLoginIn(UserBase):
    password: str
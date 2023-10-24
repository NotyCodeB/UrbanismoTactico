import sqlalchemy

from db import metadata
from models.enums import RoleType

users = sqlalchemy.Table(
    "usuarios",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("nombre", sqlalchemy.String(255)),
    sqlalchemy.Column("email", sqlalchemy.String(255), unique=True),
    sqlalchemy.Column("password", sqlalchemy.String(255)),
    sqlalchemy.Column("telefono", sqlalchemy.String(20)),
    sqlalchemy.Column("direccion", sqlalchemy.String(255)),
    sqlalchemy.Column("Rol", sqlalchemy.Enum(RoleType), nullable=False, server_default=RoleType.base.name),
)

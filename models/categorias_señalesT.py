import sqlalchemy

from db import metadata

categorias_ST = sqlalchemy.Table(
    "categorias_ST",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Nombre", sqlalchemy.String(25)),
    sqlalchemy.Column("Descripcion", sqlalchemy.String(255)),
    sqlalchemy.Column("Aplicacion", sqlalchemy.String(255))
)
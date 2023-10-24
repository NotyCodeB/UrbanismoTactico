import sqlalchemy

from db import metadata

localidades = sqlalchemy.Table(
    "localidades",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Codigo", sqlalchemy.String(25)),
    sqlalchemy.Column("Descripcion", sqlalchemy.String(255)),
    sqlalchemy.Column("Ubicacion", sqlalchemy.String(255))
)

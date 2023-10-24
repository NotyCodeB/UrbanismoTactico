import sqlalchemy

from db import metadata

situaciones_anormales = sqlalchemy.Table(
    "situaciones_anormales",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Nombre", sqlalchemy.String(25)),
    sqlalchemy.Column("TipoActorVial", sqlalchemy.String(255)),
    sqlalchemy.Column("Localidad_id", sqlalchemy.ForeignKey("localidades.id"), nullable=False),
    sqlalchemy.Column("latitud", sqlalchemy.Numeric(10, 6)),
    sqlalchemy.Column("longitud", sqlalchemy.Numeric(10, 6)),
    sqlalchemy.Column("ExistenciaSenalesTransito", sqlalchemy.Boolean)
)
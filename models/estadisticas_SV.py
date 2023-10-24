import sqlalchemy

from db import metadata

estadisticas_SV = sqlalchemy.Table(
    "estadisticas_SV",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Resporte_id", sqlalchemy.ForeignKey("situaciones_anormales.id")),
    sqlalchemy.Column("Contenido", sqlalchemy.String(255)),
    sqlalchemy.Column("TipoEstadistica", sqlalchemy.String(50)),
    sqlalchemy.Column("Responsable_id", sqlalchemy.ForeignKey("usuarios.id")),
    sqlalchemy.Column("Anio", sqlalchemy.Integer),
    sqlalchemy.Column("Mes", sqlalchemy.Integer)
)
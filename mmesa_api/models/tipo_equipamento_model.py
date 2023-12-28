from app import db


class Tipo_equipamento(db.Model):
    __tablename__ = "tipo_equipamento"

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(1000), unique=False, nullable=False)

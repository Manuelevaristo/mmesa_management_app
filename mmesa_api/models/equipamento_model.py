from app import db
from ..models import cliente_model, tipo_equipamento_model


class Equipamento(db.Model):
    __tablename__ = "equipamento"

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    model = db.Column(db.String(100), unique=False, nullable=False)
    manufacturer = db.Column(db.String(100), unique=False, nullable=False)

    problem_description = db.Column(
        db.String(1000), unique=False, nullable=False)
    input_date = db.Column(db.Date, nullable=False)
    output_date = db.Column(db.Date, nullable=False)
    repair_description = db.Column(
        db.String(1000), unique=False, nullable=False)

    equipment_type_id = db.Column(
        db.Integer, db.ForeignKey("tipo_equipamento.id"))
    owner_id = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    tipo_equipamento = db.relationship(
        tipo_equipamento_model.Tipo_equipamento, backref=db.backref("equipamentos", lazy="dynamic"))
    cliente = db.relationship(
        cliente_model.Cliente, backref=db.backref("equipamentos", lazy="dynamic"))

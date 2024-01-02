"""from app import ma
from ..models import equipamento_model
from marshmallow import fields

class EquipamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = equipamento_model.Equipamento
        load_instance = True
        fields = ("id", "name", "model", "manufacturer", "tipo_equipamento_id", "problem_description", "input_date", "output_date", "repair_description", "cliente")

    name = fields.String(required=True)
    model = fields.String(required=True)
    tipo_equipamento_id = fields.Integer(required=True)
    problem_description = fields.String(required=True)
    input_date = fields.String(required=True)
    output_date = fields.String(required=True)
    repair_description = fields.String(required=True)
    cliente = fields.Integer(required=True)
    
"""
from app import ma
from ..models import equipamento_model
from marshmallow import fields


class EquipamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = equipamento_model.Equipamento
        load_instance = True
        fields = ("id", "name", "model", "manufacturer", "tipo_equipamento",
                  "problem_description", "input_date", "output_date", "repair_description", "cliente")

    name = fields.String(required=True)
    model = fields.String(required=True)
    manufacturer = fields.String(required=True)
    problem_description = fields.String(required=True)
    input_date = fields.String(required=True)
    output_date = fields.String(required=True)
    repair_description = fields.String(required=True)
    cliente = fields.String(required=True)
    tipo_equipamento = fields.String(required=True)


"""    cliente = fields.Nested('ClienteSchema', only=("id",))  # Utilizando um campo Nested para representar a relação com Cliente
    tipo_equipamento_id = fields.Nested('Tipo_equipamentoSchema', only=("id",))  # Utilizando um campo Nested para representar o relacionamento com Tipo_equipamento
"""

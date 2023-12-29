from app import ma
from ..models import equipamento_model
from marshmallow import fields

class EquipamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = equipamento_model.Equipamento
        load_instance = True
        fields = ("id", "name", "model", "manufacturer", "equipment_type_id", "problem_description", "input_date", "output_date", "repair_description")

    name = fields.String(required=True)
    email = fields.String(required=True)
    model = fields.String(required=True)
    equipment_type_id = fields.Integer(required=True)
    problem_description = fields.String(required=True)
    input_date = fields.String(required=True)
    output_date = fields.String(required=True)
    repair_description = fields.String(required=True)
  

    
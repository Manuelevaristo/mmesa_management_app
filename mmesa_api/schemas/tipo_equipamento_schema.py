
from app import ma
from mmesa_api.schemas.equipamento_schema import EquipamentoSchema
from ..models import tipo_equipamento_model
from marshmallow import fields

class Tipo_equipamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = tipo_equipamento_model.Tipo_equipamento
        load_instance = True
        fields = ("id", "name", "description", "equipamentos")

    name = ma.auto_field(required=True)
    description = ma.auto_field(required=True)
    equipamentos = fields.List(fields.Nested(EquipamentoSchema, only=('id','name')))

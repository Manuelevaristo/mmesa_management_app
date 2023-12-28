from app import ma
from ..models import tipo_equipamento_model
from marshmallow import fields

class Tipo_equipamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = tipo_equipamento_model.Tipo_equipamento
        load_instance = True
        fields = ("id", "name","description")

    name = fields.String(required=True)
    email = fields.String(required=True)
    description = fields.String(required=True)
  
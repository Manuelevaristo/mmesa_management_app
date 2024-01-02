
from app import ma
from ..models import tipo_equipamento_model


class Tipo_equipamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = tipo_equipamento_model.Tipo_equipamento
        load_instance = True
        fields = ("id", "name", "description")

    name = ma.auto_field(required=True)
    description = ma.auto_field(required=True)

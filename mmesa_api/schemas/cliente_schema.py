from app import ma
from ..models import cliente_model
from marshmallow import fields
from ..schemas import equipamento_schema


class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = cliente_model.Cliente
        load_instance = True
        fields = ("id", "name", "email", "cell_contact",
                  "street_address", "city_address", "state_address","equipamentos")

    name = fields.String(required=True)
    email = fields.String(required=True)
    cell_contact = fields.String(required=True)
    street_address = fields.String(required=True)
    city_address = fields.String(required=True)
    state_address = fields.String(required=True)
    equipamentos = fields.List(fields.Nested(equipamento_schema.EquipamentoSchema, only=('id','name')))


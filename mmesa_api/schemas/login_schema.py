
from app import ma
from ..models import usuario_model
from marshmallow import fields

class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario
        load_instance = True
        fields = ("id", "name", "email", "senha")

    name = fields.String(required=False)
    email = fields.String(required=True)
    senha = fields.String(required=True)
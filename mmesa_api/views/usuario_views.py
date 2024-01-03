from flask_restful import Resource
from app import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entities import usuario
from ..services import usuario_service


class UsuarioList(Resource):

    def post(self):
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            email = request.json["email"]
            senha = request.json["senha"]

            novo_usuario = usuario.Usuario(
                name=name, email=email, senha=senha)
            resultado = usuario_service.cadastrar_usuario(novo_usuario)

            x = us.jsonify(resultado)
            return make_response(x, 201)


api.add_resource(UsuarioList, '/usuarios')


from flask_restful import Resource
from app import api
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services import usuario_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta


class LoginList(Resource):

    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
          
            email = request.json["email"]
            senha = request.json["senha"]
            usuario_bd = usuario_service.listar_usuario_email(email)
        if usuario_bd and usuario_bd.ver_senha(senha):
            acess_token = create_access_token(
                identity=usuario_bd.id,
                expires_delta=timedelta(seconds=100)
            )

            refresh_token = create_refresh_token(
                identity=usuario_bd.id
            )
            return make_response(jsonify({
                'acess_token':acess_token,
                'refresh_token':refresh_token,
                'message':'login realizado com sucesso',

            }), 200)
        return make_response(jsonify({
            'message': 'As credencias estão invalidas'
        }), 401)


api.add_resource(LoginList, '/login')
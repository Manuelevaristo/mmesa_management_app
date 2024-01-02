from flask_restful import Resource
from app import api
from ..schemas import tipo_equipamento_schema
from flask import request, make_response, jsonify
from ..entities import tipo_equipamento
from ..services import tipo_equipamento_service


class Tipo_equipamentoList(Resource):
    def get(self):
        tipo_equipamentos = tipo_equipamento_service.listar_tipo_equipamentos()
        te = tipo_equipamento_schema.Tipo_equipamentoSchema(many=True)
        return make_response(te.jsonify(tipo_equipamentos), 200)

    def post(self):
        te = tipo_equipamento_schema.Tipo_equipamentoSchema()
        validate = te.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]

            novo_tipo_equipamento = tipo_equipamento.Tipo_equipamento(
                name=name, description=description)
            resultado = tipo_equipamento_service.cadastrar_tipo_equipamento(
                novo_tipo_equipamento)

            x = te.jsonify(resultado)
            return make_response(x, 201)


class Tipo_equipamentoDetail(Resource):
    def get(self, id):
        tipo_equipamento = tipo_equipamento_service.listar_tipo_equipamentosById(
            id)
        if tipo_equipamento is None:
            return make_response(jsonify("tipo_equipamento não foi encontrado"), 400)

        te = tipo_equipamento_schema.Tipo_equipamentoSchema()
        return make_response(te.jsonify(tipo_equipamento), 200)

    def put(self, id):
        tipo_equipamento_bd = tipo_equipamento_service.listar_tipo_equipamentosById(
            id)
        if tipo_equipamento_bd is None:
            return make_response(jsonify("tipo_equipamento não foi encontrado"), 404)
        te = tipo_equipamento_schema.Tipo_equipamentoSchema()
        validate = te.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]

            novo_tipo_equipamento = tipo_equipamento.Tipo_equipamento(
                name=name, description=description)
            tipo_equipamento_service.actualiza_tipo_equipamento(
                tipo_equipamento_bd, novo_tipo_equipamento)
            tipo_equipamento_atualizado = tipo_equipamento_service.listar_tipo_equipamentosById(
                id)
            return make_response(te.jsonify(tipo_equipamento_atualizado), 200)

    def delete(self, id):
        tipo_equipamento_bd = tipo_equipamento_service.listar_tipo_equipamentosById(
            id)
        if tipo_equipamento_bd is None:
            return make_response(jsonify("tipo_equipamento não encontrado"), 404)

        tipo_equipamento_service.remove_tipo_equipamento(tipo_equipamento_bd)
        return make_response('Cliente excluido com sucesso!', 204)


api.add_resource(Tipo_equipamentoList, '/tipo_equipamentos')
api.add_resource(Tipo_equipamentoDetail, '/tipo_equipamentos/<int:id>')

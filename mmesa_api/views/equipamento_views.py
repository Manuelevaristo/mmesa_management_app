from flask_restful import Resource
from app import api
from ..schemas import equipamento_schema
from flask import request, make_response, jsonify
from ..entities import equipamento
from ..services import equipamento_service, cliente_service, tipo_equipamento_service
from flask_jwt_extended import jwt_required
from ..decorater import admin_requered

class EquipamentoList(Resource):

    @jwt_required()
    def get(self):
        equipamentos = equipamento_service.listar_equipamentos()
        eq = equipamento_schema.EquipamentoSchema(many=True)
        return make_response(eq.jsonify(equipamentos), 200)
    
    @admin_requered
    def post(self):
       
        eq = equipamento_schema.EquipamentoSchema()
        validate = eq.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            model = request.json["model"]
            manufacturer = request.json["manufacturer"]
            problem_description = request.json["problem_description"]
            input_date = request.json["input_date"]
            output_date = request.json["output_date"]
            repair_description = request.json["repair_description"]
            tipo_equipamento = request.json["tipo_equipamento"]
            cliente = request.json["cliente"]
            cliente_equipamento = cliente_service.listar_clientesById(cliente)
            tipo_equipamento_equipamento = tipo_equipamento_service.listar_tipo_equipamentosById(
                tipo_equipamento)
            if cliente_equipamento is None:
                return make_response(jsonify("Cliente não encontrado"), 404)
            if tipo_equipamento_equipamento is None:
                return make_response(jsonify("Tipo de equipamento não encontrado"), 404)

            novo_equipamento = equipamento.Equipamento(name=name, model=model, manufacturer=manufacturer, tipo_equipamento=tipo_equipamento_equipamento,
                                                       problem_description=problem_description, input_date=input_date, output_date=output_date, repair_description=repair_description, cliente=cliente_equipamento)
            resultado = equipamento_service.cadastrar_equipamento(
                novo_equipamento)

            x = eq.jsonify(resultado)
            return make_response(x, 201)


class EquipamentoDetail(Resource):

    @jwt_required()
    def get(self, id):
        equipamento = equipamento_service.listar_equipamentosById(id)
        if equipamento is None:
            return make_response(jsonify("equipamento não foi encontrado"), 400)

        eq = equipamento_schema.EquipamentoSchema()
        return make_response(eq.jsonify(equipamento), 200)
    
    @admin_requered
    def put(self, id):
        equipamento_bd = equipamento_service.listar_equipamentosById(id)
        if equipamento_bd is None:
            return make_response(jsonify("equipamento não foi encontrado"), 404)
        eq = equipamento_schema.EquipamentoSchema()
        validate = eq.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            model = request.json["model"]
            manufacturer = request.json["manufacturer"]
            problem_description = request.json["problem_description"]
            input_date = request.json["input_date"]
            output_date = request.json["output_date"]
            repair_description = request.json["repair_description"]
            tipo_equipamento = request.json["tipo_equipamento"]
            cliente = request.json["cliente"]
            cliente_equipamento = cliente_service.listar_clientesById(cliente)
            tipo_equipamento_equipamento = tipo_equipamento_service.listar_tipo_equipamentosById(
                tipo_equipamento)
            if cliente_equipamento is None:
                return make_response(jsonify("Cliente não encontrado"), 404)
            if tipo_equipamento_equipamento is None:
                return make_response(jsonify("Tipo de equipamento não encontrado"), 404)

            novo_equipamento = equipamento.Equipamento(name=name, model=model, manufacturer=manufacturer, tipo_equipamento=tipo_equipamento_equipamento,
                                                       problem_description=problem_description, input_date=input_date, output_date=output_date, repair_description=repair_description, cliente=cliente_equipamento)

            equipamento_service.actualiza_equipamento(
                equipamento_bd, novo_equipamento)
            equipamento_atualizado = equipamento_service.listar_equipamentosById(
                id)
            return make_response(eq.jsonify(equipamento_atualizado), 200)
        
    @admin_requered
    def delete(self, id):
        equipamento_bd = equipamento_service.listar_equipamentosById(id)
        if equipamento_bd is None:
            return make_response(jsonify("equipamento não encontrado"), 404)

        equipamento_service.remove_equipamento(equipamento_bd)
        return make_response(jsonify("equipamento excluido com sucesso!"), 204)


api.add_resource(EquipamentoList, '/equipamentos')
api.add_resource(EquipamentoDetail, '/equipamentos/<int:id>')

from flask_restful import Resource
from app import api
from ..schemas import equipamento_schema
from flask import request, make_response, jsonify
from ..entities import equipamento
from ..services import equipamento_service

class EquipamentoList(Resource):
    def get(self):
        equipamentos = equipamento_service.listar_equipamentos()
        eq = equipamento_schema.EquipamentoSchema(many=True)
        return make_response(eq.jsonify(equipamentos),200)
    
    def post(self):
        eq = equipamento_schema.EquipamentoSchema()
        validate = eq.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            name =request.json["name"]
            model = request.json["model"]
            manufacturer = request.json["manufacturer"]
            equipment_type_id = request.json["equipment_type_id"]
            problem_description = request.json["problem_description"]
            input_date = request.json["input_date"]
            output_date = request.json["output_date"]
            repair_description = request.json["repair_description"]

            novo_equipamento = equipamento.Equipamento(name=name, model=model, manufacturer = manufacturer, equipment_type_id=equipment_type_id, problem_description=problem_description, input_date=input_date, output_date=output_date, repair_description=repair_description)
            resultado = equipamento_service.cadastrar_equipamento(novo_equipamento)

            x = eq.jsonify(resultado)
            return make_response(x, 201)

class EquipamentoDetail(Resource):
    def get(self, id):
        equipamento = equipamento_service.listar_equipamentosById(id)
        if equipamento is None:
            return make_response(jsonify("equipamento não foi encontrado"), 400)

        eq = equipamento_schema.EquipamentoSchema()
        return make_response(eq.jsonify(equipamento), 200)
    
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
            equipment_type_id = request.json["equipment_type_id"]
            problem_description = request.json["problem_description"]
            input_date = request.json["input_date"]
            output_date = request.json["output_date"]
            repair_description = request.json["repair_description"]

            novo_equipamento = equipamento.Equipamento(name=name, model=model, manufacturer = manufacturer, equipment_type_id=equipment_type_id, problem_description=problem_description, input_date=input_date, output_date=output_date, repair_description=repair_description)
            equipamento_service.actualiza_equipamento(equipamento_bd, novo_equipamento)
            equipamento_atualizado = equipamento_service.listar_equipamentosById(id)
            return make_response(eq.jsonify(equipamento_atualizado), 200)
    def delete(self, id):
        equipamento_bd = equipamento_service.listar_equipamentosById(id)
        if equipamento_bd is None:
            return make_response(jsonify("equipamento não encontrado"),404)
        
        equipamento_service.remove_equipamento(equipamento_bd)
        return make_response(jsonify("equipamento excluido com sucesso!"), 204)
    
api.add_resource(EquipamentoList, '/equipamentos')
api.add_resource(EquipamentoDetail, '/equipamentos/<int:id>')
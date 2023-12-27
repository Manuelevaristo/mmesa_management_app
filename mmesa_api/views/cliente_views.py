from flask_restful import Resource
from app import api
from ..schemas import cliente_schema
from flask import request, make_response, jsonify
from ..entities import cliente
from ..services import cliente_service

class ClienteList(Resource):
    def get(self):
        clientes = cliente_service.listar_clientes()
        cl = cliente_schema.ClienteSchema(many=True)
        return make_response(cl.jsonify(clientes),200)
    
    def post(self):
        cl = cliente_schema.ClienteSchema()
        validate = cl.validate(request.json)
        if validate:
            return make_response(jsonify(validate),400)
        else:
            name =request.json["name"]
            email = request.json["email"]
            cell_contact = request.json["cell_contact"]
            street_address = request.json["street_address"]
            city_address = request.json["city_address"]
            state_address = request.json["state_address"]

            novo_cliente = cliente.Cliente(name=name, email=email, cell_contact=cell_contact, street_address=street_address, city_address=city_address, state_address=state_address)
            resultado = cliente_service.cadastrar_cliente(novo_cliente)

            x = cl.jsonify(resultado)
            return make_response(x, 201)
    
api.add_resource(ClienteList, '/clientes')
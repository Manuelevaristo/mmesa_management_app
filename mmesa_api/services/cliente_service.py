from ..models import cliente_model
from app import db

def cadastrar_cliente(cliente):
    cliente_bd = cliente_model.Cliente(name=cliente.name, email=cliente.email, cell_contact = cliente.cell_contact, street_address=cliente.street_address, city_address=cliente.city_address, state_address=cliente.state_address)
    db.session.add(cliente_bd)
    db.session.commit()
    return cliente_bd

def listar_clientes():
    clientes = cliente_model.Cliente.query.all()

    return clientes
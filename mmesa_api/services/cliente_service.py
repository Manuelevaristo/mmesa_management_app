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

def listar_clientesById(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return cliente

def actualiza_cliente(cliente_anterior, cliente_novo):
    cliente_anterior.name = cliente_novo.name
    cliente_anterior.email = cliente_novo.email
    cliente_anterior.street_address = cliente_novo.street_address
    cliente_anterior.city_address = cliente_novo.city_address
    cliente_anterior.state_address = cliente_novo.state_address
    cliente_anterior.cell_contact = cliente_novo.cell_contact
    db.session.commit()

def remove_cliente(cliente):
    db.session.delete(cliente)
    db.session.commit()
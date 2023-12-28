from ..models import tipo_equipamento_model
from app import db

def cadastrar_tipo_equipamento(tipo_equipamento):
    tipo_equipamento_bd = tipo_equipamento_model.Tipo_equipamento(name=tipo_equipamento.name, description=tipo_equipamento.description)
    db.session.add(tipo_equipamento_bd)
    db.session.commit()
    return tipo_equipamento_bd

def listar_tipo_equipamentos():
    Tipo_equipamentos = tipo_equipamento_model.Tipo_equipamento.query.all()

    return Tipo_equipamentos

def listar_tipo_equipamentosById(id):
    tipo_equipamento = tipo_equipamento_model.Tipo_equipamento.query.filter_by(id=id).first()
    return tipo_equipamento

def actualiza_tipo_equipamento(tipo_equipamento_anterior, tipo_equipamento_novo):
    tipo_equipamento_anterior.name = tipo_equipamento_novo.name
    tipo_equipamento_anterior.description = tipo_equipamento_novo.description
    db.session.commit()

def remove_tipo_equipamento(tipo_equipamento):
    db.session.delete(tipo_equipamento)
    db.session.commit()
from ..models import equipamento_model
from app import db


def cadastrar_equipamento(equipamento):
    equipamento_bd = equipamento_model.Equipamento(name=equipamento.name, model=equipamento.model, manufacturer=equipamento.manufacturer, tipo_equipamento=equipamento.tipo_equipamento,
                                                   problem_description=equipamento.problem_description, input_date=equipamento.input_date, output_date=equipamento.output_date, repair_description=equipamento.repair_description, cliente=equipamento.cliente)
    db.session.add(equipamento_bd)
    db.session.commit()
    return equipamento_bd


def listar_equipamentos():
    equipamentos = equipamento_model.Equipamento.query.all()

    return equipamentos


def listar_equipamentosById(id):
    equipamento = equipamento_model.Equipamento.query.filter_by(id=id).first()
    return equipamento


def actualiza_equipamento(equipamento_anterior, equipamento_novo):
    equipamento_anterior.name = equipamento_novo.name
    equipamento_anterior.model = equipamento_novo.model
    equipamento_anterior.manufacturer = equipamento_novo.manufacturer
    equipamento_anterior.tipo_equipamento = equipamento_novo.tipo_equipamento
    equipamento_anterior.input_date = equipamento_novo.input_date
    equipamento_anterior.output_date = equipamento_novo.output_date
    equipamento_anterior.repair_description = equipamento_novo.repair_description
    equipamento_anterior.cliente = equipamento_novo.cliente

    db.session.commit()


def remove_equipamento(equipamento):
    db.session.delete(equipamento)
    db.session.commit()

from app import db


class Equipamento(db.Model):
    __tablename__ = "equipamento"

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String(100), unique=True, nullable=False)
    model = db.Column(db.String(100), unique=False, nullable=False)
    manufacturer = db.Column(db.String(100), unique=False, nullable=False)
    equipment_type_id = db.Column(db.Integer, autoincrement=True, unique=False, nullable=False)
    problem_description = db.Column(db.String(1000), unique=False, nullable=False)
    input_date = db.Column(db.Date, nullable=False)
    output_date = db.Column(db.Date, nullable=False)
    repair_description = db.Column(db.String(1000), unique=False, nullable=False)



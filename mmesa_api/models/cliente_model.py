from app import db


class Cliente(db.Model):
    __tablename__ = "cliente"

    id = db.Column(db.Integer, primary_key=True,
                   autoincrement=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    cell_contact = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    street_address = db.Column(db.String(100), unique=False, nullable=False)
    city_address = db.Column(db.String(100), unique=False, nullable=False)
    state_address = db.Column(db.String(100), unique=False, nullable=False)


"""    def __init__(self, name, street_address, city_address, state_address, email) -> None:
        self.name = name
        self.street_address = street_address
        self.city_address = city_address
        self.state_address = state_address
        self.email = email"""

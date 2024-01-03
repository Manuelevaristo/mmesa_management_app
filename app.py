from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)
jwt = JWTManager(app)

from mmesa_api.views import cliente_views, tipo_equipamento_views, equipamento_views, usuario_views,login_views,refresh_token_views
from mmesa_api.models import cliente_model, tipo_equipamento_model, equipamento_model, usuario_model


if __name__=="__main__":

    app.run()

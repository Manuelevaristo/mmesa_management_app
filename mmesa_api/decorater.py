from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import make_response, jsonify


def admin_requered(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()

        if claims['roles'] != 'admin':
            return make_response(jsonify(message='Não é permitido esse recurso. Apenas Administradores!'), 403)
        else:
            return fn(*args, **kwargs)
    return wrapper

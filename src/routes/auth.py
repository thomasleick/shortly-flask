from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/signin', methods=['POST'])
def login():
    # Lógica de autenticação aqui
    return 'Login endpoint'

@auth_blueprint.route('/logout')
def logout():
    # Lógica de logout aqui
    return 'Logout endpoint'

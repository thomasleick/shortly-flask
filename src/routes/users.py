from flask import Blueprint

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/profile/<username>')
def user_profile(username):
    # Lógica para exibir perfil de usuário aqui
    return f'User profile: {username}'
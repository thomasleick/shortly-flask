from flask import Blueprint

urls_blueprint = Blueprint('urls', __name__)

@urls_blueprint.route('/shorten', methods=['POST'])
def shorten_url():
    # Lógica para encurtar URLs aqui
    return 'Shorten URL endpoint'

@urls_blueprint.route('/<short_code>')
def redirect_url(short_code):
    # Lógica para redirecionar URLs encurtadas aqui
    return f'Redirect to URL with code: {short_code}'
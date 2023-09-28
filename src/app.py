from flask import Flask
from flask_cors import CORS
import os
from src.configs.db_config import create_db_connection
from src.routes.auth import auth_blueprint
from src.routes.urls import urls_blueprint
from src.routes.users import users_blueprint
from src.middlewares.credentials import credentials_middleware

app = Flask(__name__)

# Habilitar o CORS para todas as rotas
CORS(app)

# Registrar o middleware de controle de credenciais
credentials_middleware(app)

# Configurar suporte para análise de dados JSON
app.config['JSON_AS_ASCII'] = False

# Registrar os Blueprints
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(urls_blueprint, url_prefix='/urls')
app.register_blueprint(users_blueprint, url_prefix='/users')

# Rota GET para "Hello, World!"
@app.route("/")
def hello_world():
    return "Hello, World!"

# Configurações e outras inicializações do aplicativo podem ser feitas aqui
# Crie uma conexão com o banco de dados
db_conn = create_db_connection()

if db_conn:
    db_cursor = db_conn.cursor()
    print('Conexão com o banco de dados efetuada com sucesso')
    # Agora você pode usar db_cursor para executar consultas SQL no banco de dados
else:
    # Trate o erro de conexão aqui, se necessário
    print('Erro na conexão com o banco de dados')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
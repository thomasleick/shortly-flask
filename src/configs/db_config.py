import os
import psycopg2

DATABASE_URL = os.environ.get('DATABASE_URL')

# Função para criar e retornar uma conexão com o banco de dados
def create_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Erro na conexão com o banco de dados: {str(e)}")
        return None
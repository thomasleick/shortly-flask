from flask import request, make_response
from src.configs.allowed_origins import allowed_origins

def credentials_middleware(app):
    @app.before_request
    def check_credentials():
        origin = request.headers.get('Origin')

        if origin in allowed_origins:
            response = make_response()
            response.headers["Access-Control-Allow-Origin"] = origin
            response.headers["Access-Control-Allow-Credentials"] = "true"
            return response

        return None
from flask import Flask #nosso app
from flask import request #recebe informações do usuário

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '12345'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

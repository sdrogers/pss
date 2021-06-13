import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect


SECRET_KEY = os.urandom(32)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    csrf = CSRFProtect()
    csrf.init_app(app) 
    from pss_app import game
    app.register_blueprint(game.bp)    
    return app
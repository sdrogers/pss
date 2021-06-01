from flask import Flask


def create_app():
    app = Flask(__name__, template_folder='pss_app/templates')
    app.debug = True
    from flaskr import app
    app.register_blueprint(app.bp)
    return app


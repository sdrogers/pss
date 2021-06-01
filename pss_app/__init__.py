from flask import Flask


def create_app():
    app = Flask(__name__)
    from pss_app import game
    app.register_blueprint(game.bp)
    return app

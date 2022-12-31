import flask
from flask_cors import CORS
from .flask_restful import Resource, Api
from .settings import DEBUG, PORT, SECRET_KEY, HOST


def make_app():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = DEBUG
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["PORT"] = PORT
    CORS(app)
    api = Api(app)
    return api, app


def run(app):
    app.run(host=HOST, port=PORT, debug=DEBUG)


api, app = make_app()

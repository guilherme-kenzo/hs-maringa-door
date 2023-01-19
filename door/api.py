from .app import api, app
from flask_restful import Resource


class BaseView(Resource):
    def get(self):
        return {"success": True}


class UserView(Resource):
    def get(self):
        return

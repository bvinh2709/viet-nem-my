from flask_restful import Resource
from config import api

class HomePage(Resource):
    def get(self):
        return {'message': 'Hello World'}

api.add_resource(HomePage, '/', endpoint='home-page')


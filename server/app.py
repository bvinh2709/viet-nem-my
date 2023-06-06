from flask import Flask, request, jsonify, make_response, session, redirect, flash
from flask_restful import Resource
from config import app, db, api

class HomePage(Resource):
    def get(self):
        return {'message': 'Hello World'}

api.add_resource(HomePage, '/', endpoint='home-page')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
from datetime import timedelta
from dotenv import load_dotenv
import os
from flask.helpers import send_from_directory

app = Flask(
    __name__,
    static_folder='client/build',
    static_url_path='',
    # static_folder='../client/build',
    # template_folder='../client/build'
    )

@app.route('/api', method=['GET'])
@cross_origin()
def index():
    return {'message': '200: Welcome to our Home Page'}, 200

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

load_dotenv()
app.secret_key = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.permanent_session_lifetime = timedelta(days=30)

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

bcrypt = Bcrypt(app)

CORS(app)
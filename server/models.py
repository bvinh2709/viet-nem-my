from sqlalchemy_serializer import SerializerMixin
from config import db

class FoodMenu(db.Model, SerializerMixin):
    __tablename__ = 'foodmenu'

    # serialize_rules = ('-orders', '-_password_hash', '-password_confirmation',)

    id = db.Column( db.Integer, primary_key = True )
    name = db.Column( db.String )
    image = db.Column ( db.String )
    price = db.Column( db.Float )
from flask_restful import Resource
from config import api, db
from models import FoodMenu
from flask import make_response, request


class FoodMenus(Resource):
    def get(self):
        fitems = [fi.to_dict() for fi in FoodMenu.query.all()]
        return make_response( fitems, 200)

    def post(self):
        data = request.get_json()

        new_item = FoodMenu(
            name = data['name'],
            image = data['image'],
            price = data['price'],
        )

        db.session.add(new_item)
        db.session.commit()

        return make_response(new_item.to_dict(), 201)

class FoodMenuById(Resource):
    def get(self, id):
        return make_response((FoodMenu.query.filter(FoodMenu.id==id).first()).to_dict(), 200)

    def patch(self, id):
        data = request.get_json()

        fitem = FoodMenu.query.filter(FoodMenu.id == id).first()
        for key in data.keys():
            setattr(fitem, key, data[key])
        db.session.add(fitem)
        db.session.commit()

        return make_response(fitem.to_dict(), 200)

    def delete(self, id):
        fitem = FoodMenu.query.filter(FoodMenu.id == id).first()

        db.session.delete(fitem)
        db.session.commit()

        return {'message': 'this food is deleted'}

api.add_resource(FoodMenus, '/menu', endpoint='menu')
api.add_resource(FoodMenuById, '/menu/<int:id>')


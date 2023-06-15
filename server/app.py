from flask import Flask, request, jsonify, make_response, session, redirect, flash
from flask_restful import Resource
from config import app, db
# from models import User, FoodMenu, Order
from apis import home_page, food_menu

home_page
food_menu

if __name__ == '__main__':
    app.run(port=5555, debug=True)
from app import app
from models import db, FoodMenu

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")

        FoodMenu.query.delete()

        fi1 = FoodMenu(name='Egg Roll', price ='5.99', image='https://images.unsplash.com/photo-1559095240-55a16b2dda6a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZWdnJTIwcm9sbHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60')
        fitems = [fi1]
        db.session.add_all(fitems)
        db.session.commit()

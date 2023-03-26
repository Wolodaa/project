from app import *


with app.app_context():
   db.create_all()
   # db.drop_all() #видалення усіх таблиць

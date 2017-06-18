from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

# 'mysql+pymysql://flaskdemo:flaskdemo@flaskdemo.cwsaehb7ywmi.us-east-1.rds.amazonaws.com:3306/flaskdemo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://akshay1234:akshay7272@udemy.cjyjj0rgxaie.us-west-2.rds.amazonaws.com:3306/udemydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'akshay7272'
api = Api(app)


@app.before_first_request
def create_tables():
	db.create_all()

jwt = JWT(app, authenticate, identity) # /auth


api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
	from db import db
	db.init_app(app)  #we are importing here due to circular imports
	app.run(port=5000, debug=True)
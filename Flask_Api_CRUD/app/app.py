from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity 
from resources.user import UserRegister 
from resources.item import Item, ItemAll
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = 'Mike'
api = Api(app)

@app.before_first_request
def create_table():
  db.create_all() 

jwt = JWT(app, authenticate, identity)


#This is a better approche of setting a endpoint with a resource 
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')    
api.add_resource(ItemAll, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')
if __name__ == '__main__':
  #circuler importing
  from db import db
  db.init_app(app)
#To get detail of the errors always keep debug=True
  app.run(port=8002, debug=True)



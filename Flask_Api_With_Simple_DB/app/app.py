from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity 
from user import UserRegister 
from item import Item, ItemAll


app = Flask(__name__)
app.secret_key = 'Mike'
api = Api(app)

jwt = JWT(app, authenticate, identity)

#This is a better approche of setting a endpoint with a resource 
api.add_resource(Item, '/item/<string:name>')    
api.add_resource(ItemAll, '/items')
api.add_resource(UserRegister, '/register')
if __name__ == '__main__':
#To get detail of the errors always keep debug=True
  app.run(port=8002, debug=True)



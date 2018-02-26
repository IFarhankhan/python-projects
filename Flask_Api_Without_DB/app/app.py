from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity 
app = Flask(__name__)
app.secret_key = '1234k'
api = Api(app)

#user authentication

jwt = JWT(app, authenticate, identity) 

#Using in memory list

items = []

#Clearing endpoints from cluter unique Resources for each endpoint.  
class itemList(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Please")

#First endpoint .
    @jwt_required()
    def get (self, name):

        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

#Second  endpoint.
    def post(self, name):

        if next(filter(lambda x: x['name'] == name, items), None):
           return{'message':"An item with name '{}' already exists.".format(name)}

        request_data = itemList.parser.parse_args()
        item = {'name': name, 'price': request_data ['price']}
        items.append(item)
        return item, 201

    def delete(self, name):

        global items 
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):

        request_data = itemList.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None: 
            item = {'name': name, 'price': request_data['price']}
            items.append(item)
        else: 
            item.update(request_data)
        return item     



#Listing all items.    
class itemAll(Resource):
    def get(self):
        return('items', items)

#This is a better approche of setting a endpoint with a resource 
api.add_resource(itemList, '/item/<string:name>')    
api.add_resource(itemAll, '/items')

#To get detail of the errors always keep debug=True
app.run(port=8002, debug=True)


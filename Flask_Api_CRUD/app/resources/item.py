from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Please")

    parser.add_argument('store_id', type=float, required=True, help="Store Id")
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Not found'}, 404


    def post(self, name):
        if self.find_by_name(name):
           return {'message': "Name '{}' already exists.".format(name)}
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
          item.save_to_db()
        except:
            return {'message': "Errors "}
        return item, 201 
    
    
    

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Deleted'} 

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name) 

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()

#Listing all items
class ItemAll(Resource):
    def get(self):

      return {'item': list(map(lambda x: x.json(),ItemModel.query.all()))}

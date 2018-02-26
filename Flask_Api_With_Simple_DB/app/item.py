import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Please")

    @jwt_required()
    def get(self, name):
        item = self.find_by_name(name)
        if item:
            return item
        return {'message': 'Not found'}, 404

    #Second  endpoint.
    @classmethod
    def find_by_name(cls, name):
      connection = sqlite3.connect('data.db')
      cursor = connection.cursor()
      query = "SELECT * FROM items WHERE name=?"
      result = cursor.execute(query, (name,))
      raw = result.fetchone()
      connection.close()
      if row:
        return{'item': {'name': row[0], 'price': row[1]}}

    def post(self, name):
        if self.find_by_name(name):
           return {'message': "Name '{}' already exists.".format(name)}
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        try:
          self.insert(item)
        except:
            return {'message': "Errors "}
        return item, 201 
    
    
    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES(?, ?)"
        cursor.execute(query,  (item['name'], item['price']))
        connection.commit()
        connection.close()
    
    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query,  (item['price'], item['name']))
        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
        return {'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name) 
        update_item = {'name': name, 'price': data['price']}

        if item is None:
            self.insert(update_item)
        else:
            self.update(update_item)
        return update_item

#Listing all items
class ItemAll(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = curser.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})
        connection.close()
        return {'items': items}


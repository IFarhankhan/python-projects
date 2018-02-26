from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


#Simple python  rest api 
stores = [

    {

        'name': 'This store',
        'items': [
            {
                'name': 'That Item',
                'price': 24.23

            }

        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

#POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data =request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/name:string
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'no entry found'})    


#GET /store "List "
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

#POST /store/<string:name>/item {name:, price} "Creating"
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data ['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'item cannot be added'})


#GET /store/<string:name>/item "Veiwing "
@app.route('/store/<string:name>/items')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'no item here check the list boy'})    


app.run(port=8001)

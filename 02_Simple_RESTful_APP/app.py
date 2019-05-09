from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [{
    'name': 'Seven Eleven',
    'items': [{
        'name': 'Bread',
        'price': 4.99
    }]
}]


@app.route('/')
def index():
    return render_template('index.html')


# Post /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {'name': request_data['name'], 'items': []}
    stores.append(new_store)
    return jsonify(new_store)


# Get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


# Get /store
@app.route('/store')
def get_stores():
    return jsonify(stores)


# Post /store/<string:name>/item data: {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': float(request_data['price'])
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# Get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'store not found'})


if __name__ == '__main__':
    app.run(debug=True)
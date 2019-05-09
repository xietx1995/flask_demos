from flask import Flask

app = Flask(__name__)

stores = [{
    'name': 'Seven Eleven',
    'items': [{
        'name': 'Bread',
        'price': 4.99
    }]
}]


# Post /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# Get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass


# Get /store
@app.route('/store')
def get_stores(name):
    pass


# Post /store/<string:name>/item data: {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


# Get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass
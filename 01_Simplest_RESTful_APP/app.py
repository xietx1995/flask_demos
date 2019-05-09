from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class ItemList(Resource):
    def get(self):
        return {'items': items}, 200


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {
                'message':
                'An item with name "{}" already exists.'.format(name)
            }, 400
        req_data = request.get_json()
        item = {'name': name, 'price': req_data['price']}
        items.append(item)
        return item, 201


api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')

app.run(port=5000, debug=True)
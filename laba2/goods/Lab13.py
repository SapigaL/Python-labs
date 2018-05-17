from flask import Flask, abort
from flask_restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__, static_url_path="")
api = Api(app)

goods = [
    {
        'Id': 0,
        'name': 'Default',
        'price': 0.0,
        'weight': 0,

    }
]

goods_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'weight': fields.Integer,
    'price': fields.Float,

}


class GoodsList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, required=True, help='No Id provided', location='json')
        self.reqparse.add_argument('name', type=str, default="", location='json')
        self.reqparse.add_argument('price', type=float, default=0, location='json')
        self.reqparse.add_argument('weight', type=int, default=0, location='json')
        super(GoodsList, self).__init__()

    @staticmethod
    def get():
        return {'All goods available': [marshal(good, goods_fields) for good in goods]}

    def put(self):
        args = self.reqparse.parse_args()
        good = {
            'Id': goods[-1]['Id'] + 1,
            'id': args['id'],
            'name': args['name'],
            'price': args['price'],
            'weight': args['weight'],
            }
        goods.append(good)
        return {'Good': marshal(good, goods_fields)}, 201

    def post(self):
        args = self.reqparse.parse_args()
        good = [good for good in goods if good.get('id') == args['id']]
        if len(good) == 0:
            abort(404)
        good = good[0]
        args = self.reqparse.parse_args()
        for namber, v in args.items():
            if v is not None:
                good[namber] = v
        return {'Good': marshal(good, goods_fields)}


class Good(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('id', type=int, location='json')
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('price', type=float, location='json')
        self.reqparse.add_argument('weight', type=int, location='json')
        super(Good, self).__init__()

    def get(self, id):
        good = [good for good in goods if good.get('id') == id]
        if len(good) == 0:
            abort(404)
        return {'Good': marshal(good[0], goods_fields)}

    def delete(self, id):
        good = [good for good in goods if good.get('id') == id]
        if len(good) == 0:
            abort(404)
        goods.remove(good[0])
        return {'result': True}


api.add_resource(GoodsList, '/goods', endpoint='goods')
api.add_resource(Good, '/goods/<int:id>', endpoint='good')

if __name__ == '__main__':
    app.run(debug=True)
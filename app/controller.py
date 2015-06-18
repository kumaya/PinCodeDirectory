from app import app
from models import postalinfo
from flask_restful import Resource, Api, abort

api = Api(app)

FAKE_DATA = [
             {
              'id': 1,
              'name': 'mayank'},
             {
              'id': 2,
              'name': 'vikram'}
             ]

def abort_if_res_non_existant(res_id):
    if res_id > len(FAKE_DATA):
        abort(404,
              message=('Resource with id: %s does not exist' % res_id))


class PinCodes(Resource):
    def get(self):
        return postalinfo.query.all

    def post(self):
        pass


class PinCode(Resource):
    def get(self, res_id):
#         abort_if_res_non_existant(int(res_id))
        from flask import jsonify
        val = jsonify(postalinfo.query.get(int(res_id)))
        print val
        return val

    def delete(self, res_id):
        pass

    def put(self, res_id):
        pass

api.add_resource(PinCodes, '/rest/pincodes')
api.add_resource(PinCode, '/rest/pincodes/<res_id>')
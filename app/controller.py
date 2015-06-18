from app import app
from models import postalinfo
from flask_restful import Resource, Api, abort

api = Api(app)

def abort_if_res_non_existant(res_id):
    if res_id > len(FAKE_DATA):
        abort(404,
              message=('Resource with id: %s does not exist' % res_id))


class PinCodes(Resource):
    def get(self):
        return [{"pincode": x.pincode, "officename": x.officename} for x in postalinfo.query.filter().all()]

    def post(self):
        pass


class PinCode(Resource):
    def get(self, res_id):
#         abort_if_res_non_existant(int(res_id))
        val = postalinfo.query.filter().get(res_id)
        return {"Postal Index Number": res_id,
                "Office Name": val.officename,
                "Office Type": val.officeType,
                "Delivery Status": val.Deliverystatus,
                "Division Name": val.divisionname,
                "Region Name": val.regionname,
                "Circle Name": val.circlename,
                "Taluk": val.Taluk,
                "District Name": val.Districtname,
                "State Name": val.statename}

    def delete(self, res_id):
        pass

    def put(self, res_id):
        pass

api.add_resource(PinCodes, '/rest/pincodes')
api.add_resource(PinCode, '/rest/pincodes/<res_id>')
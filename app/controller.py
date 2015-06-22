from app import app
from models import postalinfo
from flask_restful import Resource, Api
from flask import request

api = Api(app)


class PinCodes(Resource):
    def get(self):
        query = postalinfo.query
        page = request.args.get('page', 1)
        per_page = request.args.get('size', 50)
        yo = []
        if page == 1 or per_page == 50:
            help_str = ("Enter query as http://<URI>?page=<page_no>&size="
                        "<per_page> to get particular page and items per page")
            yo.append(help_str)
        vals = query.paginate(int(page), int(per_page))
        some = {}
        for val in vals.items:
            some["Postal Index Number"] = val.pincode
            some["Office Name"] = val.officename
            some["Office Type"] = val.officeType
            some["Delivery Status"] = val.Deliverystatus
            some["Division Name"] = val.divisionname
            some["Region Name"] = val.regionname
            some["Circle Name"] = val.circlename
            some["Taluk"] = val.Taluk
            some["District Name"] = val.Districtname
            some["State Name"] = val.statename
            yo.append(some)
        return yo

    def post(self):
        pass


class PinCode(Resource):
    def get(self, res_id):
        val = postalinfo.query.filter().get_or_404(res_id)
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
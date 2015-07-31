from app import db


class postalinfo(db.Model):
    pincode = db.Column(db.Integer, primary_key=True)
    officename = db.Column(db.String(255))
    officeType = db.Column(db.String(10))
    Deliverystatus = db.Column(db.String(255))
    divisionname = db.Column(db.String(255))
    regionname = db.Column(db.String(255))
    circlename = db.Column(db.String(255))
    Taluk = db.Column(db.String(255))
    Districtname = db.Column(db.String(255))
    statename = db.Column(db.String(255))

    def __init__(self, *kwargs):
        kwargs = kwargs[0]
        self.pincode = kwargs.get('pincode')
        self.officename = kwargs.get('officename', None)
        self.officeType = kwargs.get('officeType', None)
        self.Deliverystatus = kwargs.get('Deliverystatus', None)
        self.divisionname = kwargs.get('divisionname')
        self.regionname = kwargs.get('regionname')
        self.circlename = kwargs.get('circlename')
        self.Taluk = kwargs.get('Taluk')
        self.Districtname = kwargs.get('Districtname')
        self.statename = kwargs.get('statename')

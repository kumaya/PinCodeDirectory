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

#     def __repr__(self):
#         return (self.officename)

    def to_json(self):
        pass
from taskmanager import db

# class FundingArea(db.Model):
#     # schema for FundingArea model
#     id = db.Column(db.Integer, primary_key=True)
#     fund_area_name = db.Column(db.String(35), unique=True, nullable=False)

#     def __repr__(self):
#         return self.fund_area_name

# class OperationArea(db.Model):
#     # schema for OperationArea model
#     id = db.Column(db.Integer, primary_key=True)
#     op_area_name = db.Column(db.String(25), nullable=False)

#     def __repr__(self):
#         return self.op_area_name

class Trust(db.Model):
    # schema for Trust model
    id = db.Column(db.Integer, primary_key=True)
    trust_name = db.Column(db.String(60), unique=True, nullable=False)
    trust_description = db.Column(db.Text, nullable=True)
    trust_reg_num = db.Column(db.Integer, unique=True, nullable=False)
    trust_phone = db.Column(db.Integer)
    trust_email = db.Column(db.String(70))
    trustee_names = db.Column(db.Text)
    trust_apply = db.Column(db.Text)
    funding_type = db.Column(db.String(35))
    funding_area = db.Column(db.String(25))

    def __repr__(self):
        return self.trust_name
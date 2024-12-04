from trustdatabase import db

class Region(db.Model):
    # schema for FundingArea model
    id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(35), unique=True, nullable=False)
    trusts = db.relationship("Trust", backref="region", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.region_name

class Cause(db.Model):
    # schema for OperationArea model
    id = db.Column(db.Integer, primary_key=True)
    cause_name = db.Column(db.String(25), nullable=False)
    trusts = db.relationship("Trust", backref="cause", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.cause_name

class Trust(db.Model):
    # schema for Trust model
    id = db.Column(db.Integer, primary_key=True)
    trust_reg_num = db.Column(db.Integer, unique=True, nullable=False)
    trust_name = db.Column(db.String(60), unique=True, nullable=False)
    trust_description = db.Column(db.Text, nullable=True)
    trust_phone = db.Column(db.Integer)
    trust_email = db.Column(db.String(70))
    trustee_names = db.Column(db.Text)
    trust_apply = db.Column(db.Text)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id", ondelete="CASCADE"), nullable=False)
    cause_id = db.Column(db.Integer, db.ForeignKey("cause.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return self.trust_name
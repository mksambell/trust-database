from trustdatabase import db

class Region(db.Model):
    # schema for Region model
    id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(35), unique=True, nullable=False)
    trusts = db.relationship("Trust", backref="region", cascade="all, delete", lazy=True)

    def __repr__(self):
        return self.region_name

class Trust(db.Model):
    # schema for Trust model
    id = db.Column(db.Integer, primary_key=True)
    trust_reg_num = db.Column(db.Integer, unique=True, nullable=False)
    trust_name = db.Column(db.String(60), unique=True, nullable=False)
    trust_description = db.Column(db.Text, nullable=True)
    trust_phone = db.Column(db.String(11))
    trust_email = db.Column(db.String(100))
    trustee_names = db.Column(db.Text)
    region_id = db.Column(db.Integer, db.ForeignKey("region.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return self.trust_name
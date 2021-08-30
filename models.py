from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class CandidateModel(db.Model):
    __tablename__ = 'candidate'

    candidate_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(100))
    mobile_number = db.Column(db.String(20))

    def __init__(self, full_name, age, email, mobile_number):
        self.full_name = full_name
        self.age = age
        self.email = email
        self.mobile_number = mobile_number

    def __repr__(self):
        return f"{self.candidate_id}:{self.full_name}:{self.age}"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


prim_sec_skills_association_table = db.Table('primary_secondary_map', db.Model.metadata,
                                             db.Column('psid', db.Integer, db.ForeignKey('primary_skills.psid')),
                                             db.Column('ssid', db.Integer, db.ForeignKey('secondary_skills.ssid'))
                                             )


class PrimarySkillsModel(db.Model):
    __tablename__ = 'primary_skills'

    psid = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100))
    secondary_skills = db.relationship("SecondarySkillsModel",
                                       secondary=prim_sec_skills_association_table)

    def __init__(self, skill_name):
        self.skill_name = skill_name

    def __repr__(self):
        return f"{self.skill_name}:{[c.as_dict() for c in self.secondary_skills]}"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class SecondarySkillsModel(db.Model):
    __tablename__ = 'secondary_skills'

    ssid = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(100))

    def __init__(self, skill_name, common_skill):
        self.skill_name = skill_name

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

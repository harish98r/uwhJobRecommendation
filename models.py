from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = 'employee_info'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    course = db.Column(db.String(100))

    def __init__(self, employee_id, name, age, course):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.course = course

    def __repr__(self):
        return f"{self.employee_id}:{self.name}:{self.age}:{self.course}"

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
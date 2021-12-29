
import flask
from flask import Flask, jsonify
from models import db, CandidateModel, PrimarySkillsModel, SecondarySkillsModel

import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://***/hackathon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "***"

db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/data', methods=['POST'])
def create():
    input_data = flask.request.json
    full_name = input_data['full_name']
    age = input_data['age']
    email = input_data['email']
    mobile_number = input_data['mobile_number']
    candidate = CandidateModel(full_name=full_name, age=age, email=email, mobile_number=mobile_number)
    db.session.add(candidate)
    db.session.commit()
    return candidate.as_dict()


@app.route("/data", methods=['GET'])
def getAllCandidates():
    json_data = []
    for u in CandidateModel.query.all():
        json_data.append(u.as_dict())
    return json.dumps(json_data)


@app.route('/data/<int:id>', methods=['GET'])
def getCandidateById(id):
    candidate = CandidateModel.query.filter_by(candidate_id=id).first()
    if candidate:
        return json.dumps(candidate.as_dict())
    return f"Employee with id ={id} Doesn't exist"


@app.route('/data/<int:id>', methods=['PUT'])
def update(id):
    candidate = CandidateModel.query.filter_by(candidate_id=id).first()
    if candidate:
        input_data = flask.request.json
        candidate.full_name = input_data['full_name']
        candidate.age = input_data['age']
        candidate.email = input_data['email']
        candidate.mobile_number = input_data['mobile_number']
        db.session.commit()
        return json.dumps(candidate.as_dict())
    return f"Employee with id = {id} Doesn't exist"


@app.route('/data/<int:id>', methods=['DELETE'])
def delete(id):
    candidate = CandidateModel.query.filter_by(candidate_id=id).first()
    if candidate:
        db.session.delete(candidate)
        db.session.commit()
        return json.dumps(candidate.as_dict())
    return f"Employee Delete Failed"


@app.route('/skills', methods=['POST'])
def createskills():
    input_data = flask.request.json
    full_name = input_data['jjj']
    age = input_data['age']
    email = input_data['email']
    mobile_number = input_data['mobile_number']
    candidate = CandidateModel(full_name=full_name, age=age, email=email, mobile_number=mobile_number)
    db.session.add(candidate)
    db.session.commit()
    return candidate.as_dict()


@app.route("/skills", methods=['GET'])
def getskills():
    json_data = []
    u = PrimarySkillsModel.query.all()
    return repr(u)


@app.route("/skills/<int:id>", methods=['GET'])
def getSecondarySkills():
    json_data = []
    for u in PrimarySkillsModel.query.all():
         json_data.append(u.as_dict())
         for v in u.secondary_skills:
             json_data.append(v.as_dict())

    return json.dumps(json_data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='localhost', port=5000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

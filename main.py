from os import abort

import flask
from flask import Flask, render_template, request, redirect
from models import db, EmployeeModel

import mariadb
import sys
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Cuckoo123@mariadb-1.cldbrv6wfk2y.ap-south-1.rds.amazonaws.com/hackathon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "***"

db.init_app(app)

# config = {
#     'host': 'mariadb-1.cldbrv6wfk2y.ap-south-1.rds.amazonaws.com',
#     'port': 3306,
#     'user': 'admin',
#     'password': 'Cuckoo123',
#     'database': 'hackathon'
# }
# try:
#     conn =mariadb.connect(**config)
# except mariadb.Error as e:
#     print("Error connection to MariaDB")
#     sys.exit(1)
#
# cur = conn.cursor()
#
# @app.route('/data', methods=['GET'])
# def getList():
#     cur.execute("select * from youth")
#     row_headers = [x[0] for x in cur.description]
#     rv = cur.fetchall()
#     json_data = []
#     for result in rv:
#         json_data.append(dict(zip(row_headers, result)))
#     name = 'harish'
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint
#     return json.dumps(json_data)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/data', methods=['POST'])
def create():
        input_data = flask.request.json
        employee_id = input_data['employee_id']
        name = input_data['name']
        age = input_data['age']
        course = input_data['course']
        employee = EmployeeModel(employee_id=employee_id, name=name, age=age, course=course)
        db.session.add(employee)
        db.session.commit()
        return employee.as_dict()

@app.route("/data", methods=['GET'])
def retriveData():
    json_data = []
    for u in EmployeeModel.query.all():
        json_data.append(u.as_dict())
    return json.dumps(json_data)

@app.route('/data/<int:id>', methods=['GET'])
def RetrieveEmployee(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if employee:
        return json.dumps(employee.as_dict())
    return f"Employee with id ={id} Doesn't exist"


@app.route('/data/<int:id>', methods=['PUT'])
def update(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if employee:
        input_data = flask.request.json
        employee.employee_id = input_data['employee_id']
        employee.name = input_data['name']
        employee.age = input_data['age']
        employee.course = input_data['course']
        db.session.commit()
        return json.dumps(employee.as_dict())
    return f"Employee with id = {id} Doesn't exist"

@app.route('/data/<int:id>', methods=['DELETE'])
def delete(id):
    employee = EmployeeModel.query.filter_by(id=id).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
        return json.dumps(employee.as_dict())
    return f"Employee Delete Failed"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='localhost', port=5000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

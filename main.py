from flask import Flask
from models import db, EmployeeModel

import mariadb
import sys
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Cuckoo123@mariadb-1.cldbrv6wfk2y.ap-south-1.rds.amazonaws.com/hackathon'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "***"
db.init_app(app)

config = {
    'host': 'mariadb-1.cldbrv6wfk2y.ap-south-1.rds.amazonaws.com',
    'port': 3306,
    'user': 'admin',
    'password': 'Cuckoo123',
    'database': 'hackathon'
}
try:
    conn =mariadb.connect(**config)
except mariadb.Error as e:
    print("Error connection to MariaDB")
    sys.exit(1)

cur = conn.cursor()

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/data', methods=['GET'])
def getList():
    cur.execute("select * from youth")
    row_headers = [x[0] for x in cur.description]
    rv = cur.fetchall()
    json_data = []
    for result in rv:
        json_data.append(dict(zip(row_headers, result)))
    name = 'harish'
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint
    return json.dumps(json_data)

@app.route("/data2", methods=['GET'])
def retriveData():
    json_data = []
    for u in EmployeeModel.query.all():
        json_data.append(u.as_dict())
    return json.dumps(json_data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host='localhost', port=5000)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from flask import Flask, jsonify, abort, make_response, request
#import Accountant, Analyzer, DBManager, Group, ObsCoManager, User, Variables
#from DBManager import DBManager
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/obsco"
mongo = PyMongo(app)

users = [
    {
        'name': u'Jason Statham',
        'id': 12345671,
        'groups': [1,2,3,4],
        'email': u'statham@hollywood.com',
        'password': u'cokguclusifre',
        'age': 45,
        'superuser': True,
        'title': u'Chairman',
        'skills': [{
             "id": 1,
             "value": 10
            },
            {
             "id": 4,
             "value": 8
            },
            {
             "id": 8,
             "value": 10
            },
            {
             "id": 6,
             "value": 6
            },
            {
             "id": 13,
             "value": 10
            }
        ],
    },
    {
        'name': u'Eminem',
        'id': 12345672,
        'groups': [2,3],
        'email': u'eminem@hollywood.com',
        'password': u'musedinliyorum',
        'age': 45,
        'superuser': False,
        'title': u'Instructor',
        'skills': [{
             "id": 4,
             "value": 10
            },
            {
             "id": 5,
             "value": 10
            },
            {
             "id": 8,
             "value": 7
            },
            {
             "id": 9,
             "value": 8
            },
            {
             "id": 10,
             "value": 7
            }
        ],
        'done': False
    }
]

groups = [
    {
            "id":1,
            "name":"Instructors",
            "members":[12345671,12345672,12345673]
    },
    {
            "id":2,
            "name":"Orchestrion",
            "members":[21400527,21400528,21400529,21400530,21400531]
    }
]

#man = DBManager()
#val = man.fetchUser(userId=12345671)

@app.route('/')
def hello_world():
    return 'ObsCo initialized'

@app.route('/obsco/api/v1.0/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

@app.route('/obsco/api/v1.0/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.route('/obsco/api/v1.0/groups', methods=['GET'])
def get_groups():
    return jsonify({'groups': groups})

@app.route('/obsco/api/v1.0/groups/<int:group_id>', methods=['GET'])
def get_group(group_id):
    group = [group for group in groups if group['id'] == group_id]
    if len(group) == 0:
        abort(404)
    return jsonify({'group': group[0]})

@app.route('/obsco/api/v1.0/dbusers', methods=['GET'])
def get_dbusers():
    online_users = mongo.db.users.find({"id": 12345671},{'_id':0})
    x = [i for i in online_users]
    return jsonify({"index.html": x})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run()

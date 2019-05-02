from flask import Flask, jsonify, abort, make_response, request
#import Accountant, Analyzer, DBManager, Group, ObsCoManager, User, Variables

app = Flask(__name__)

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

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run()

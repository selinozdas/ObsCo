from flask import Flask, jsonify, abort, make_response, request
#import Accountant, Analyzer, DBManager, Group, ObsCoManager, User, Variables
#from DBManager import DBManager
from flask_pymongo import PyMongo
from db import mongo
import DBManager

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/obsco"
mongo.init_app(app)

man = DBManager.DBManager()
#val = man.fetchUser(userId=12345671)

@app.route('/')
def hello_world():
    return 'ObsCo initialized'

@app.route('/obsco/api/v1.0/users/<int:userId>', methods=['GET'])
def get_user(name = '', userId = -1):
    results = man.fetchUser(userId=userId)
    return jsonify({'users': results})

@app.route('/obsco/api/v1.0/groups/<int:group>', methods=['GET'])
def get_group(group, name="")->list:
    group_members = man.getGroup(group)
    return jsonify({'groups': group_members})

@app.route('/obsco/api/v1.0/skills/<int:userId>', methods=['GET'])
def get_skill(userId, skill = -1)->list:
    skill_list = man.getSkill(userId)
    return jsonify({'skills': skill_list})

@app.route('/obsco/api/v1.0/cansee/<int:userId>/<int:group>', methods=['GET'])
def can_see(userId,group):
    see = man.canSee(userId,group)
    return jsonify({'canSee': see})
'''
@app.route('/obsco/api/v1.0/skills/addskill/', methods=['POST', 'GET'])
def add_skill():
    mongo.db.skills.findOne({$query: {}, $orderby: {$natural: -1}} )
    id = request.args.get('id', None)
    name = request.args.get('name', None)
    return jsonify({'id': id}, {'name': name})
'''

'''
@app.route('/obsco/api/v1.0/groups/<int:group_id>', methods=['GET'])
def get_groups(group_id):
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
'''
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run()

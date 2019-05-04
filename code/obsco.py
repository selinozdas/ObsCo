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
    results = man.fetchUser(userId)
    return jsonify({'users': results})

@app.route('/obsco/api/v1.0/groups/<int:group>', methods=['GET'])
def get_group(group, name="")->list:
    """
        Lists the users in the group.
        
        Keyword Arguments:
        group -- unique id of the group (non-optional)
        name -- name of the group for search queries (default "")
        
        Return Value:
        user_list -- list of users in the group 
    """
    groups = mongo.db.groups.find({'id':group},{'_id':0})
    g = [x for x in groups]
    userID_list = g[0]['members']
    user_list = []
    if len(userID_list) == 0:
        abort(404)
    elif len(userID_list) != 0:
        for entry in userID_list:
            curs_user = mongo.db.users.find({'id':entry},{'_id':0})
            user = [i for i in curs_user]
            user_list = user_list + user
    return jsonify({'groups': user_list})

@app.route('/obsco/api/v1.0/skills/<int:userId>', methods=['GET'])
def get_skill(userId, skill = -1)->list:
    """
        Finds the specified skill information of a user, if it is not entered returns all skills of the user.
        
        Keyword Arguments:
        userId -- unique id of the user (non-optional)
        skill -- unique id of the skill (default -1)
        
        Return Value:
        skill_temp -- skill information if skill id is given else all skills of the given user 
    """
    #fetch user
    try:
        curs_user = mongo.db.users.find({'id':userId},{'_id':0})
        user = [i for i in curs_user]
    except:
        user = []
    if len(user) == 0:
        abort(404)
    elif (len(user) != 0):
        skills = user[0]['skills']
        skill_temp = -1
        for entry in skills:
            if(skill == entry["id"]):
                skill_temp = entry
                if (skill_temp == -1):
                    abort(404)
                    #raise Exception("No such skill exist for the given user")
                else:
                    jsonify({'skills': skill_temp})
            else:
                return jsonify({'skills': skills})

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

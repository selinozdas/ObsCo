from flask import Flask, jsonify, abort, make_response, request
#import Accountant, Analyzer, DBManager, Group, ObsCoManager, User, Variables
#from DBManager import DBManager
from flask_pymongo import PyMongo
from db import mongo
import DBManager as dbm

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/obsco"
mongo.init_app(app)


@app.route('/')
def hello_world():
    return 'ObsCo initialized'


@app.route('/obsco/api/v1.0/users/<int:userId>', methods=['GET'])
def get_user(name = '', userId = -1):
    results = dbm.fetchUser(userId=userId)
    return jsonify({'users': results})


@app.route('/obsco/api/v1.0/groups/<int:group>', methods=['GET'])
def get_group(group, name="")->list:
    group_members = dbm.getGroup(group)
    return jsonify({'groups': group_members})


@app.route('/obsco/api/v1.0/skills/<int:userId>', methods=['GET'])
def get_skill(userId, skill = -1)->list:
    '''
        returns skills of a user
    '''
    skill_list = dbm.getSkill(userId)
    return jsonify({'skills': skill_list})


@app.route('/obsco/api/v1.0/cansee/<int:userId>/<int:group>', methods=['GET'])
def can_see(userId,group):
    '''
    returns 1 if user can see relations
    '''
    see = dbm.canSee(userId,group)
    return jsonify({'canSee': see})


@app.route('/obsco/api/v1.0/groupname/<int:id>', methods=['GET'])
def get_gname(id):
    '''
    returns the group name with the specific id
    '''
    name = dbm.getGroupName(id)
    return jsonify({'name': name})


@app.route('/obsco/api/v1.0/skilllist', methods=['GET'])
def get_skill_list():
    '''
    returns all skills in db
    '''
    name = dbm.getSkillList()
    return jsonify({'skills': name})

@app.route('/obsco/api/v1.0/recommender/<int:id>/<int:nu>/<skills>', methods=['GET'])
def get_recommendation(id,nu,skills):

    skill_list = skills.split('_')
    skill_list = [int(i) for i in skill_list]
    recommended = dbm.recommend(id,skill_list,nu)
    return jsonify({'recommendation': recommended})

@app.route('/obsco/api/v1.0/groupmembers/<int:group>', methods=['GET'])
def get_group_members(group)->list:
    group_members = dbm.getGroupMembers(group)
    return jsonify({'members': group_members})

@app.route('/obsco/api/v1.0/addskill/<name>', methods=['GET'])
def add_user(name):
    '''
    add skill into db with the given name
    '''
    processed_name = name.replace('_',' ')
    response = dbm.addSkill(processed_name)
    return jsonify({'isAdded': response})

@app.route('/obsco/api/v1.0/reputation/<int:id>', methods=['GET'])
def get_total_reputation(id):
    average_reputation = dbm.getTotalReputation(id)
    return jsonify({'reputation': average_reputation})

@app.route('/obsco/api/v1.0/groupreputation/<int:id>/<int:group>', methods=['GET'])
def get_group_reputation(id,group):
    average_reputation = dbm.getGroupReputation(id,group)
    return jsonify({'reputation': average_reputation})

@app.route('/obsco/api/v1.0/grouprelations/<int:id>/<int:group>', methods=['GET'])
def get_group_relations(id,group):
    average_reputation = dbm.getRelations(id,group)
    return jsonify({'relations': average_reputation})

@app.route('/obsco/api/v1.0/sentiment/<int:voter>/<int:voted>/<entry>', methods=['GET'])
def add_nlp_entry(voter,voted,entry):
    x = dbm.addNLPVote(voter,voted,str(entry))
    return jsonify({'relations': x})

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
    app.run(debug=True)

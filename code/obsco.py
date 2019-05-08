from flask import Flask, jsonify, abort, make_response, request, send_file
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
    result = dbm.addNLPVote(voter,voted,str(entry))
    return jsonify({'relations': result})

@app.route('/obsco/api/v1.0/eligiblemembers/<int:id>', methods=['GET'])
def get_eligible(id):
    result = dbm.getGroups(id)
    return jsonify({'eligible': result})

@app.route('/obsco/api/v1.0/creategroup/<name>/<int:owner>/<members>', methods=['GET'])
def create_group(name,owner,members):
    result = dbm.createGroup(name,owner,members)
    return jsonify({'creation': result})

@app.route('/obsco/api/v1.0/addleader/<int:owner>/<int:group>/<members>', methods=['GET'])
def add_leader(owner,group,members):
    result = dbm.addLeader(owner,group,members)
    return jsonify({'added': result})

@app.route('/obsco/api/v1.0/changepassword/<int:id>/<password>', methods=['GET'])
def change_pwd(id,password):
    result = dbm.changePassword(id,password)
    return jsonify({'changed': result})

@app.route('/obsco/api/v1.0/get_image')
def get_image():
    filename = 'default_profile_pic.jpg'
    return send_file(filename, mimetype='image')

@app.route('/obsco/api/v1.0/voteskill/<int:voter>/<int:voted>/<int:skill>/<int:vote>', methods=['GET'])
def vote_skill(voter,voted,skill,vote):
    result = dbm.voteSkill(voted,skill,vote)
    return jsonify({'voted': result})
@app.route('/obsco/api/v1.0/votesre', methods=['GET'])
def reassign_all():
    result = dbm.reassignAll()
    return jsonify({'voted': result})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(threaded = True,debug=True)

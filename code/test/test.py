from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/obsco"
from db import mongo
mongo.init_app(app)
import dbmanagertest
man = dbmanagertest.dbmanagertest()
@app.route('/users/<int:userId>', methods=['GET'])
def get_user(name='', userId=-1):
    results = man.fetchUser(userId=userId)
    return jsonify({'users': results})

@app.route("/skills/<int:userId>", methods=['GET'])
def get_skill(userId, skill=-1) -> list:
    """
        Finds the specified skill information of a user, if it is not entered returns all skills of the user.

        Keyword Arguments:
        userId -- unique id of the user (non-optional)
        skill -- unique id of the skill (default -1)

        Return Value:
        skill_temp -- skill information if skill id is given else all skills of the given user
    """
    # fetch user
    try:
        curs_user = mongo.db.users.find({'id': userId}, {'_id': 0})
        user = [i for i in curs_user]
    except:
        user = []
    if (len(user) != 0):
        skills = user[0]['skills']
        skill_temp = -1
        for entry in skills:
            if (skill == entry["id"]):
                skill_temp = entry
                if (skill_temp == -1):
                    raise Exception("No such skill exist for the given user")
                else:
                    jsonify({'skills': skill_temp})
            else:
                return jsonify({'skills': skills})

@app.route("/test", methods=['GET'])
def get_test():
    import dbmanagertest
    man = dbmanagertest.dbmanagertest()
    x = man.fetchUser(userId=12345671)


    return jsonify({'x': x}, {'_id':0})

if __name__ == '__main__':
    app.run()


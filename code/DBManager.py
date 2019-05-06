import User
from helpers import quick_sort,get_variances
from pprint import pprint
from db import mongo
import numpy as np


def fetchUser(name="", userId=-1) -> list:
    """
        Fetch user with the given ID from DB.

        Keyword arguments:
        name -- name of the user which can be used for search (default "")
        userId -- unique id of the user (default -1)

        Return Value:
        results -- list of users with the given credentials
    """
    users = mongo.db.users
    results = []

    # No query for invalid calls
    if (name == "" and userId == -1):
        return []

    # function call with userId
    elif (userId != -1):
        for entry in users.find({'id':userId},{'_id':0}):
            if (int(entry["id"]) == int(userId)):
                results.append(entry)

    # function call with only name
    elif (str(name) != ""):
        split_name = "".join(name.split())
        split_name = split_name.lower()
        for entry in users.find(({},{'_id':0})):
            temp_entry = entry["name"].lower()
            temp_entry = "".join(temp_entry.split())
            if (split_name in temp_entry):
                results.append(entry)
    # if no result can be found
    if (len(results) == 0):
        return []
    return results


def getSkill(userId, skill=-1) -> list:
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
        user = fetchUser(userId=userId)
    except:
        user = []

    skill_temp = -1
    # get skills if user is found
    if (len(user) != 0):
        for u in user:
            if (skill != -1):
                for entry in u["skills"]:
                    if (skill == entry["id"]):
                        skill_temp = entry
                if (skill_temp == -1):
                    return "No such skill exist for the given user"
                else:
                    return skill_temp
            else:
                skill_temp =  u["skills"]
                for i in skill_temp:
                    name = getSkillName(i['id'])
                    i['name'] = name
    return skill_temp


def getGroup(group: int, name="") -> list:
    """
        Lists the members of the group.

        Keyword Arguments:
        group -- unique id of the group (non-optional)
        name -- name of the group for search queries (default "")

        Return Value:
        user_list -- list of users in the group
    """
    groups = mongo.db.groups.find({'id':group},{'_id':0})
    userID_list = []
    user_list = []
    for entry in groups:
        print(entry['members'])
        if entry["id"] == group:
            userID_list = userID_list + entry["members"]
    if len(userID_list) != 0:
        for entry in userID_list:
            x = fetchUser(userId=entry)
            user_list = user_list + x
    return user_list


def canSee(userId,group):
    user_list = fetchUser(userId=userId)
    val = 0
    user = user_list[0]
    groups = user['groups']
    for g in groups:
        if g['id'] == group:
            val = g['leaders']
    return val


def getGroupName( group:int):
    groups = mongo.db.groups.find({'id':group},{'_id':0})
    group_list = [i for i in groups]
    return group_list[0]['name']


def getSkillName( skill:int):
    '''
    returns the name of the skill with given id
    '''
    skills = mongo.db.skills.find({'id':skill},{'_id':0})
    skill_list = [i for i in skills]
    return skill_list[0]['name']


def analysisInfo(groupId:int):
    '''
        Returns the information that is going to be used for recommender
    '''
    members = getGroup(groupId)
    member_list = []
    for member in members:
        entry = {member['id']: member['skills']}
        member_list.append(entry)
    return member_list


def getSkillLength():
    '''
        Returns the total number of skills
    '''
    skills = mongo.db.skills.find({},{'_id':0})
    skills = [skill for skill in skills]
    return(len(skills))


def getSkillList():
    '''
        Returns a list of dictionary of the skills with {id:name} key value pairs 
    '''
    skills = mongo.db.skills.find({},{'_id':0})
    result = []
    for entry in skills:
        temp = {entry['id']:entry['name']}
        result.append(temp)
    return result

def recommender(info,skills,mem_count):
    column_nu = getSkillLength()
    member_nu = len(info)
    matrix = np.zeros(shape = (member_nu,column_nu),dtype = int)
    column_names = list(range(1,column_nu+1))
    row_names = []
    for entry in info:
        row_names= row_names + list([i for i in entry.keys()])
    skill_list = []
    for entry in info:
        skill_list= skill_list + list([i for i in entry.values()])
    row = 0
    for member in skill_list:
        for skill in member:
            column = skill['id']-1
            matrix[row,column]= skill['value']
        row += 1

    variances = get_variances(matrix)

    column_name_map = {}
    for i in range(len(column_names)):
        column_name_map[column_names[i]] = i

    skill_indexes = []
    for i in range(len(skills)):
        if skills[i] in column_name_map:
            skill_indexes.append(column_name_map[skills[i]])

    if len(skill_indexes) == 0:
        print("No skills found")
        return []

    ranks = []

    for i in range(member_nu):
        rank = 0

        for s in skill_indexes:
            rank += matrix[i][s] * variances[s]

        ranks.append(rank)

    rank_index = quick_sort(ranks, is_ascending=False)
    if mem_count > member_nu:
        mem_count = member_nu   
    result = []
    for i in range(mem_count):
        entry = {row_names[rank_index[i]]: ranks[i]}
        result.append(entry)
    return result


def recommend(group,skills,mem_nu):
    '''
    '''
    info = analysisInfo(group)
    recommended  = recommender(info,skills,mem_nu)
    members = []
    
    for i in recommended:
        user_list = fetchUser(userId=list(i.keys())[0])
        user = user_list[0]
        temp = {}
        temp['id'] = user['id']
        temp['name'] = user['name']
        temp['recommended'] = float(format(list(i.values())[0],'.2f'))
        members.append(temp)
    return members
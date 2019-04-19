import User
from pymongo import MongoClient
from pprint import pprint

class DBManager:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["obsco"]
    
    
    #fetches user according to the given id or name and returns the list of users. This function enables name searching for search engine.
    def fetchUser(self, name = "", userId = -1)->list:
        """
            Fetch user with the given ID from DB.
            
            Keyword arguments:
            name -- name of the user which can be used for search (default "")
            userId -- unique id of the user (default -1)
            
            Return Value:
            results -- list of users with the given credentials
        """
        users = self.db["users"]
        results = []
        
        #No query for invalid calls
        if (name == "" and userId == -1):
            raise Exception("You need to enter the name or the ID of the user.")
        
        #function call with userId
        elif (userId != -1) :
            for entry in users.find():
                if (int(entry["id"]) == int(userId)):
                    results.append(entry) 

        #function call with only name
        elif (str(name) != "") :
            split_name = "".join(name.split())
            split_name = split_name.lower()
            for entry in users.find():
                temp_entry = entry["name"].lower()
                temp_entry = "".join(temp_entry.split())
                if (split_name in temp_entry):
                    results.append(entry)
        #if no result can be found
        if (len(results)==0):
            raise Exception("No user has been found with the given credentials.")
        return results
    
    #returns the specified skill if entered as parameter, else returns all of the skills that the user with the ID has
    def getSkill(self, userId, skill = -1)->list:
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
            user = self.fetchUser(userId=userId)
        except:
            user = []
        
        skill_temp = -1
        #get skills if user is found
        if (len(user) != 0):
            for u in user:
                if (skill != -1):
                    for entry in u["skills"]:
                        if(skill == entry["id"]):
                            skill_temp = entry
                    if (skill_temp == -1):
                        raise Exception("No such skill exist for the given user")
                    else:
                        return skill_temp
                else:
                    return u["skills"]
        return skill_temp


    def getAnswers(self, form:int, user: User):
        return


    def getGroup(self, group:int, name="")->list:
        """
            Lists the users in the group.
            
            Keyword Arguments:
            group -- unique id of the group (non-optional)
            name -- name of the group for search queries (default "")
            
            Return Value:
            user_list -- list of users in the group 
        """
        groups = self.db["groups"].find()
        userID_list = []
        user_list = []
        for entry in groups:
            if entry["id"] == group:
                userID_list = userID_list + entry["members"]
        if len(userID_list) != 0:
            for entry in userID_list:
                x = self.fetchUser(userId=entry)
                user_list = user_list + x
        return user_list

    def setUser(self, id:int, name:str):
        return

    def setAnswer(self, form:int, user: User):
        return

    def setGroup(self, group:str, groupId:int, users:list):
        return

    def connectServer(self, id:int):
        return

    def addRequest(self, id:int, group:int):
        return

    def removeRequest(self, id:int, group:int):
        return

    def addReport(self, id:int, group:int):
        return

    def searchUser(self, name:str, id:int):
        return

    def searchGroup(self, name:str, id:int):
        return

    def searchForm(self, user: User, form:int):
        return

    def acceptRequest(self, id:int, group:int):
        return


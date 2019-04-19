import User
from pymongo import MongoClient

class DBManager:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["obsco"]
    
    
    #fetches user according to the given id or name and returns the list of users. This function enables name searching for search engine.
    def fetchUser(self, name = "", userId = -1):
        users = self.db["users"]
        results = []
        
        #No query for in valid calls
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
        
        if (len(results)==0):
            raise Exception("No user has been found with the given credentials.")
        return results
    
    #returns the specified skill if entered as parameter, else returns all of the skills that the user with the ID has
    def getSkill(self, userId, skill = -1):
        try:
            user = self.fetchUser(userId=userId)
        except:
            user = []
        skill_temp = -1
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

    def getGroup(self, group:int, name=""):
        groups = self.db["groups"]
        
        return

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

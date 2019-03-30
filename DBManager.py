import User


class DBManager:
    def __init__(self, db, col, query):
        self.db = db
        self.col = col
        self.query = query

    def fetchUserDataFromDB(self, name:str, userId:int):
        return

    def getForm(self, form:int, user: User):
        return

    def getAnswers(self, form:int, user: User):
        return

    def getGroup(self, group:int, name:str):
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

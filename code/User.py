import Accountant, Group
from Variables import GROUP_EDIT


class User:
    def __init__(self, name, mail, id, password, groups, age, gender, corporateID, title, rank):
        self.name = name
        self.mail = mail
        self.id = id
        self.password = password
        self.groups = groups
        self.age = age
        self.gender = gender
        self.corporateID = corporateID
        self.title = title
        self.rank = rank

    def getSubordinateInfo(self, userId:int, name:str):
        return

    def pushForm(self, formId:int, group:int):
        #send a form to fill to all group members
        return

    def fillForm(self, formType:int):
        return

    def requestAccess(self, group:int):
        return

    def reportBug(self, report:str):
        return

    def showGroup(self, group:int):
        return

    def createGroup(self, name:str, groupid:int, users:list):
        if self.rank < GROUP_EDIT:
            return 0
        group = Group(name, groupid, users)
        self.groups.append(group)
        return 1

    def changeProfileInfo(self, changeRequestReceiver:Accountant):
        return

    def deleteGroup(self, group:Group):
        if self.rank < GROUP_EDIT:
            return 0
        self.groups.remove(group)
        return 1

    def showUserData(self, name:str, id:int):
        return

    def showDataGroup(self, name:str, group:int):
        return

    def showAnotherUser(self, id:int, name:str):
        return

    # def showComponents(self, userToShow:User):
        # return

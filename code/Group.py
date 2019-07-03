import User


class Group:
    def __init__(self, name, groupid, members):
        self.name = name
        self.groupid = groupid
        self.members = members

    members = []

    def addMember(self, user: User):
        if user in self.members:
            self.members.append(user)
            return 0
        else:
            return -1

    def deleteMember(self, user: User):
        self.members.remove(user)

    def viewMember(self, user: User):
        if user in self.members:
            return user
        else:
            return -1

    def viewGroup(self, user: User):
        return

    def offerMember(self, count:int):
        return

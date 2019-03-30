import User


class Group:
    def __init__(self, name, id, members):
        self.name = name
        self.id = id
        self.members = members

    def addMember(self, user: User):
        self.members.append(user)

    def deleteMember(self, user: User):
        self.members.remove(user)

    def viewMember(self, user: User):
        return

    def viewGroup(self, user: User):
        return

    def offerMember(self, count:int):
        return

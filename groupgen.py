from pymongo import MongoClient

client = MongoClient()

db = client["obsco"]

db.groups.insert_many([
    {
        "id":1,
        "name":"Instructors",
        "members":[12345671,12345672,12345673]
    },
    {
        "id":2,
        "name":"Orchestrion",
        "members":[21400527,21400528,21400529,21400530,21400531]
    },
    {
        "id":3,
        "name":"ObsCo",
        "members":[21400537,21400538,21400539,21400540,21400541]
    },
    {
        "id":4,
        "name":"Warp",
        "members":[21400517,21400518,21400519,21400520,21400521]
    },
    {
        "id":5,
        "name":"Back-End",
        "members":[21400537,21400538,21400539]
    },
    {
        "id":6,
        "name":"Front-End",
        "members":[21400538,21400540,21400541]
    },
])

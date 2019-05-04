from pymongo import MongoClient
#change url
mongo_url = 'mongodb://127.0.0.1:29618/'
client = MongoClient(mongo_url)

db = client["obsco"]

db.groups.insert_many([
    {
        "id":1,
        "name":"Instructors",
        "members":[12345671,12345672,12345673],
        "owner": 12345671,
        "leaders": [12345671]
        
    },
    {
        "id":2,
        "name":"Orchestrion",
        "members":[21400527,21400528,21400529,21400530,21400531],
        "owner":12345672,
        'leaders':[12345672, 21400527]
    },
    {
        "id":3,
        "name":"ObsCo",
        "members":[21400537,21400538,21400539,21400540,21400541],
        'owner':12345671,
        'leaders':[12345671,21400537]
    },
    {
        "id":4,
        "name":"Warp",
        "members":[21400517,21400518,21400519,21400520,21400521],
        'owner':12345673,
        'leaders':[12345673,21400517]

    },
    {
        "id":5,
        "name":"Back-End",
        "members":[21400537,21400538,21400539],
        'owner':21400537,
        'leaders':[21400537]
    },
    {
        "id":6,
        "name":"Front-End",
        "members":[21400538,21400540,21400541],
        'owner':21400538,
        'leaders':[21400538]

    },
        {
        "id":7,
        "name":"Students",
        "members":[21400527,21400528,21400529,21400530,21400531,21400537,21400538,21400539,21400540,21400541,21400517,21400518,21400519,21400520,21400521],
        "owner": 12345671,
        "leaders": [12345671,12345672,12345673]
        
    },
])

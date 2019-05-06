from pymongo import MongoClient
#change url
mongo_url = 'mongodb://127.0.0.1:29298/'
client = MongoClient(mongo_url)

db = client["obsco"]

db.users.insert_many(
[
    {   "name" : "Halil Altay Guvenir",
        "id": 12345671,
        "groups" : [
            {'id':1,
            'members':1,
            'owner':1,
            'leaders':1},
            {'id':2,
            'members':0,
            'owner':0,
            'leaders':1},
            {'id':3,
            'members':0,
            'owner':1,
            'leaders':1},
            {'id':4,
            'members':0,
            'owner':0,
            'leaders':1},
            {'id':7,
            'members':0,
            'owner':1,
            'leaders':1}
        ],
        "email" : "guvenir@cs.bilkent.edu.tr",
        "password" : "cokguclusifre",
        "age" : 45,
        "superuser" : True,
        "title" : "Chairman",
        "skills":[{
             "id": 1,
             "value": 10
            },
            {
             "id": 4,
             "value": 8
            },
            {
             "id": 8,
             "value": 10
            },
            {
             "id": 6,
             "value": 6
            },
            {
             "id": 13,
             "value": 10
            }
        ]
    },
    {   "name" : "A. Ercument Cicek",
        "id": 12345672,
        "groups" : [
            {'id':1,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':2,
            'members':0,
            'owner':1,
            'leaders':1},
            {'id':7,
            'members':0,
            'owner':0,
            'leaders':1}
        ],
        "email" : "cicek@cs.bilkent.edu.tr",
        "password": "musedinliyorum",
        "age" : 45,
        "superuser" : False,
        "title" : "Instructor",
        "skills":[{
             "id": 4,
             "value": 10
            },
            {
             "id": 5,
             "value": 10
            },
            {
             "id": 8,
             "value": 7
            },
            {
             "id": 9,
             "value": 8
            },
            {
             "id": 10,
             "value": 7
            }
        ]
    },
    {   "name" : "Hamdi Dibeklioglu",
        "id": 12345673,
        "groups" : [
            {'id':1,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':4,
            'members':0,
            'owner':1,
            'leaders':1},
            {'id':7,
            'members':0,
            'owner':0,
            'leaders':1}
        ],
        "email" : "dibeklioglu@cs.bilkent.edu.tr",
        "password" : "diplernink",
        "age" : 45,
        "superuser" : False,
        "title" : "Instructor",
        "skills":[{
             "id": 6,
             "value": 10
            },
            {
             "id": 4,
             "value": 9
            },
            {
             "id": 7,
             "value": 10
            },
            {
             "id": 9,
             "value": 8
            },
            {
             "id": 12,
             "value": 7
            }
        ]
    },
    {   "name" : "Selin Ozdas",
        "id": 21400537,
       "groups" : [
            {'id':3,
            'members':1,
            'owner':0,
            'leaders':1},
            {'id':5,
            'members':1,
            'owner':1,
            'leaders':1},
            {'id':7,
            'members':1,
            'owner':0,
            'leaders':0}
        ],
        "email" : "selin.ozdas@ug.bilkent.edu.tr",
        "password" : "banaismailde",
        "age" : 25,
        "superuser" : False,
        "title" : "Student",
        "skills":[{
             "id": 1,
             "value": 7
            },
            {
             "id": 2,
             "value": 8
            },
            {
             "id": 3,
             "value": 9
            },
            {
             "id": 14,
             "value": 4
            },
            {
             "id": 13,
             "value": 7
            }
        ]
    },
    {   "name" : "Dogan Can Eren",
        "id": 21400538,
       "groups" : [
            {'id':3,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':5,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':6,
            'members':1,
            'owner':1,
            'leaders':1},
            {'id':7,
            'members':1,
            'owner':0,
            'leaders':0}
        ],
        "email" : "can.eren@ug.bilkent.edu.tr",
        "password" : "atesim39acikti",
        "age" : 25,
        "superuser" : False,
        "title" : "Student",
        "skills":[{
             "id": 1,
             "value": 8
            },
            {
             "id": 2,
             "value": 5
            },
            {
             "id": 9,
             "value": 7
            },
            {
             "id": 14,
             "value": 8
            },
            {
             "id": 13,
             "value": 6
            }
        ]
    },
    {   "name" : "Ceren Uysal",
        "id": 21400539,
       "groups" : [
            {'id':3,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':5,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':7,
            'members':1,
            'owner':0,
            'leaders':0}
        ],
        "email" : "ceren.uysal@ug.bilkent.edu.tr",
        "password" : "buhayatiseviyorum",
        "age" : 25,
        "superuser" : False,
        "title" : "Student",
        "skills":[{
             "id": 1,
             "value": 4
            },
            {
             "id": 2,
             "value": 7
            },
            {
             "id": 9,
             "value": 7
            },
            {
             "id": 10,
             "value": 8
            },
            {
             "id": 13,
             "value": 5
            }
        ]
    },
    {   "name" : "A. Mahir Ozer",
        "id": 21400540,
        "groups" : [
            {'id':3,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':6,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':7,
            'members':1,
            'owner':0,
            'leaders':0}
        ],
        "email" : "mahir.ozer@ug.bilkent.edu.tr",
        "password" : "fotosopbilirim",
        "age" : 25,
        "superuser" : False,
        "title" : "Student",
        "skills":[{
             "id": 1,
             "value": 6
            },
            {
             "id": 2,
             "value": 4
            },
            {
             "id": 9,
             "value": 8
            },
            {
             "id": 10,
             "value": 7
            },
            {
             "id": 14,
             "value": 9
            }
        ]
    },
    {   "name" : "Berk Erzin",
        "id": 21400541,
        "groups" : [
            {'id':3,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':6,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':7,
            'members':1,
            'owner':0,
            'leaders':0}
        ],
        "email" : "berk.erzin@ug.bilkent.edu.tr",
        "password" : "orumcekadam",
        "age" : 25,
        "superuser" : False,
        "title" : "Student",
        "skills":[{
             "id": 1,
             "value": 5
            },
            {
             "id": 3,
             "value": 3
            },
            {
             "id": 9,
             "value": 8
            },
            {
             "id": 10,
             "value": 8
            },
            {
             "id": 13,
             "value": 6
            }
        ]
    },
    {   "name" : "Serhat Aras",
        "id": 21400517,
        "groups" : [
            {'id':4,
            'members':1,
            'owner':0,
            'leaders':1},
            {'id':7,
            'members':1,
            'owner':0,
            'leaders':0},
            {'id':11,
            'members':1,
            'owner':1,
            'leaders':1}
        ],
        "email" : "serhat.aras@ug.bilkent.edu.tr",
        "password" : "ilovecoding",
        "age" : 22,
        "superuser" : False,
        "title" : "Student",
        "skills":[{
             "id": 1,
             "value": 5
            },
            {
             "id": 2,
             "value": 6
            },
            {
             "id": 10,
             "value": 5
            },
            {
             "id": 13,
             "value": 7
            }
        ]
    }
]
)
from pymongo import MongoClient

client = MongoClient()

db = client["obsco"]

db.users.insert_many(
[
    {   "name" : "Halil Altay Guvenir",
        "id": 12345671,
        "groups" : [
            1,2,3,4
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
            2,3
        ],
        "email" : "cicek@cs.bilkent.edu.tr",
        "password" : "musedinliyorum",
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
            3,4
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
            5
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
            5,6
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
            
        ],
        "email" : "berk.erzin@ug.bilkent.edu.tr",
        "password" : "orumcekadam",
        "age" : 25,
        "superuser" : True,
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
    }

]
)
from pymongo import MongoClient
#change url
mongo_url = 'mongodb://127.0.0.1:29618/'
client = MongoClient(mongo_url)

db = client["obsco"]

db.skills.insert_many([
    {
        "id":1,
        "name":"Project Management",
        "users":[
            {
             "id": 12345671,
             "value": 10
            },
            {
             "id": 21400537,
             "value": 7
            },
            {
             "id": 21400538,
             "value": 8
            },
            {
             "id": 21400539,
             "value": 4
            },
            {
             "id": 21400540,
             "value": 6
            },
            {
             "id": 21400541,
             "value": 5
            },
            {
             "id": 21400517,
             "value": 5
            }
        ]
    },
    {
        "id":2,
        "name":"Python",
        "users":[
            {
             "id": 21400537,
             "value": 8
            },
            {
             "id": 21400538,
             "value": 5
            },
            {
             "id": 21400539,
             "value": 7
            },
            {
             "id": 21400540,
             "value": 5
            },
            {
             "id": 21400517,
             "value": 6
            },
            {
             "id": 21400518,
             "value": 7
            }
        ]
    },
    {
        "id":3,
        "name":"MongoDB",
        "users":[
            {
             "id": 21400537,
             "value": 8
            },
            {
             "id": 21400541,
             "value": 3
            }
        ]
    },
    {
        "id":4,
        "name":"Machine Learning",
        "users":[
            {
             "id": 12345671,
             "value": 8
            },
            {
             "id": 12345672,
             "value": 10
            },
            {
             "id": 12345673,
             "value": 9
            },
            {
             "id": 21400518,
             "value": 8
            },
            {
             "id": 21400519,
             "value": 6
            }
        ]
    },
    {
        "id":5,
        "name":"Bioinformatics",
        "users":[
            {
             "id": 12345672,
             "value": 10
            }
        ]

    },
    {
        "id":6,
        "name":"Computer Vision",
        "users":[
            {
             "id": 12345671,
             "value": 6
            },
            {
             "id": 12345673,
             "value": 10
            },
            {
             "id": 21400518,
             "value": 6
            },
            {
             "id": 21400519,
             "value": 8
            }
        ]
    },
    {
        "id":7,
        "name":"Pattern Recognition",
        "users":[
            {
             "id": 12345673,
             "value": 10
            }
        ]
    },
    {
        "id":8,
        "name":"Data Mining",
        "users":[
            {
             "id": 12345671,
             "value": 10
            },
            {
             "id": 12345672,
             "value": 7
            }
        ]
    },
    {
        "id":9,
        "name":"Algorithms",
        "users":[
            {
             "id": 12345672,
             "value": 8
            },
            {
             "id": 12345673,
             "value": 8
            },
            {
             "id": 21400538,
             "value": 7
            },
            {
             "id": 21400539,
             "value": 7
            },
            {
             "id": 21400540,
             "value": 6
            },
            {
             "id": 21400541,
             "value": 8
            },
            {
             "id": 21400518,
             "value": 7
            },
            {
             "id": 21400519,
             "value": 5
            }
        ]
    },
    {
        "id":10,
        "name":"Problem Solving",
        "users":[
            {
             "id": 12345672,
             "value": 7
            },
            {
             "id": 21400539,
             "value": 8
            },
            {
             "id": 21400540,
             "value": 7
            },
            {
             "id": 21400541,
             "value": 8
            },
            {
             "id": 21400517,
             "value": 5
            }
        ]
    },
    {
        "id":11,
        "name":"Persuasion",
        "users":[
        ]
    },
    {
        "id":12,
        "name":"Public Speaking",
        "users":[
            {
             "id": 12345673,
             "value": 7
            }
        ]
    },
    {
        "id":13,
        "name":"Leadership",
        "users":[
            {
             "id": 12345671,
             "value": 10
            },
            {
             "id": 21400537,
             "value": 7
            },
            {
             "id": 21400538,
             "value": 6
            },
            {
             "id": 21400539,
             "value": 5
            },
            {
             "id": 21400541,
             "value": 6
            },
            {
             "id": 21400517,
             "value": 7
            }
        ]
    },
      {
        "id":14,
        "name":"Android Development",
        "users":[
            {
             "id": 21400538,
             "value": 8
            },
            {
             "id": 21400537,
             "value": 4
            },
            {
             "id": 21400540,
             "value": 9
            }
        ]

    }
])

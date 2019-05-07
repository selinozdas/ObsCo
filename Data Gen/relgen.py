from pymongo import MongoClient
#change url
mongo_url = 'mongodb://127.0.0.1:27017/'
client = MongoClient()
db = client['obsco']

db.relations.insert_many([
    {
        'voter':12345671,
        'voted':12345672,
        'votes':[1,1,1,1,1,0,0,1,1]
    },
    {
        'voter':12345671,
        'voted':12345673,
        'votes':[1,1,1,0,1]
    },
    {
        'voter': 12345672,
        'voted': 12345671,
        'votes': [1,1,1,1,1,1,1,1,1,0]
    },
    {
        'voter': 12345672,
        'voted': 12345673,
        'votes': [1,0,1,1,1]
    },
    {
        'voter': 12345673,
        'voted': 12345671,
        'votes': [1,1,1,1,1,1]
    },
    {
        'voter': 12345673,
        'voted': 12345672,
        'votes': [0,1,1,1,1,0,1,1,1]
    },
    {
        'voter': 12345671,
        'voted': 21400537,
        'votes': [1,1,0,1,0,0,0,1,0,1,1,1,0]
    },
    {
        'voter': 12345671,
        'voted': 21400538,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400539,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400540,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400541,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400537,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400538,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400539,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400540,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400541,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400537,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400538,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400539,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400540,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400541,
        'votes': []
    },
    {
        'voter': 21400537,
        'voted': 21400538,
        'votes': []
    },
    {
        'voter': 21400537,
        'voted': 21400539,
        'votes': []
    },
    {
        'voter': 21400537,
        'voted': 21400540,
        'votes': []
    },
    {
        'voter': 21400537,
        'voted': 21400541,
        'votes': []
    },
    {
        'voter': 21400538,
        'voted': 21400537,
        'votes': []
    },
    {
        'voter': 21400538,
        'voted': 21400539,
        'votes': []
    },
    {
        'voter': 21400538,
        'voted': 21400540,
        'votes': []
    },
    {
        'voter': 21400538,
        'voted': 21400541,
        'votes': []
    },
    {
        'voter': 21400539,
        'voted': 21400537,
        'votes': []
    },
    {
        'voter': 21400539,
        'voted': 21400538,
        'votes': []
    },
    {
        'voter': 21400539,
        'voted': 21400540,
        'votes': []
    },
    {
        'voter': 21400539,
        'voted': 21400541,
        'votes': []
    },
    {
        'voter': 21400540,
        'voted': 21400537,
        'votes': []
    },
    {
        'voter': 21400540,
        'voted': 21400538,
        'votes': []
    },
    {
        'voter': 21400540,
        'voted': 21400539,
        'votes': []
    },
    {
        'voter': 21400540,
        'voted': 21400541,
        'votes': []
    },
    {
        'voter': 21400541,
        'voted': 21400537,
        'votes': []
    },
    {
        'voter': 21400541,
        'voted': 21400538,
        'votes': []
    },
    {
        'voter': 21400541,
        'voted': 21400539,
        'votes': []
    },
    {
        'voter': 21400541,
        'voted': 21400540,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400517,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400518,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400519,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400517,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400518,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400519,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400517,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400518,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400519,
        'votes': []
    },
    {
        'voter': 21400517,
        'voted': 21400518,
        'votes': []
    },
    {
        'voter': 21400517,
        'voted': 21400519,
        'votes': []
    },
    {
        'voter': 21400518,
        'voted': 21400517,
        'votes': []
    },
    {
        'voter': 21400518,
        'voted': 21400519,
        'votes': []
    },
{
        'voter': 21400519,
        'voted': 21400517,
        'votes': []
    },
    {
        'voter': 21400519,
        'voted': 21400518,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400527,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400528,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400529,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400530,
        'votes': []
    },
    {
        'voter': 12345671,
        'voted': 21400531,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400527,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400528,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400529,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400530,
        'votes': []
    },
    {
        'voter': 12345672,
        'voted': 21400531,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400527,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400528,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400529,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400530,
        'votes': []
    },
    {
        'voter': 12345673,
        'voted': 21400531,
        'votes': []
    },
    {
        'voter': 21400527,
        'voted': 21400528,
        'votes': []
    },
    {
        'voter': 21400527,
        'voted': 21400529,
        'votes': []
    },
    {
        'voter': 21400527,
        'voted': 21400530,
        'votes': []
    },
    {
        'voter': 21400527,
        'voted': 21400531,
        'votes': []
    },
    {
        'voter': 21400528,
        'voted': 21400527,
        'votes': []
    },
    {
        'voter': 21400528,
        'voted': 21400529,
        'votes': []
    },
    {
        'voter': 21400528,
        'voted': 21400530,
        'votes': []
    },
    {
        'voter': 21400528,
        'voted': 21400531,
        'votes': []
    },
    {
        'voter': 21400529,
        'voted': 21400527,
        'votes': []
    },
    {
        'voter': 21400529,
        'voted': 21400528,
        'votes': []
    },
    {
        'voter': 21400529,
        'voted': 21400530,
        'votes': []
    },
    {
        'voter': 21400529,
        'voted': 21400531,
        'votes': []
    },
    {
        'voter': 21400530,
        'voted': 21400527,
        'votes': []
    },
    {
        'voter': 21400530,
        'voted': 21400528,
        'votes': []
    },
    {
        'voter': 21400530,
        'voted': 21400529,
        'votes': []
    },
    {
        'voter': 21400530,
        'voted': 21400531,
        'votes': []
    },
    {
        'voter': 21400531,
        'voted': 21400527,
        'votes': []
    },
    {
        'voter': 21400531,
        'voted': 21400528,
        'votes': []
    },
    {
        'voter': 21400531,
        'voted': 21400529,
        'votes': []
    },
    {
        'voter': 21400531,
        'voted': 21400530,
        'votes': []
    }
])
from pymongo import MongoClient

client = MongoClient()
db = client['obsco']
db.votes.insert_many([
    {
        'id':12345671,
        'skill':1,
        'points': [9,10,7,7,8,8,9]
    }
])

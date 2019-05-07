from pymongo import MongoClient

client = MongoClient()
db = client['obsco']
db.votes.insert_many([
    #ALTAY
    {
        'id':12345671,
        'skill':1,
        'points': [9,10,7,7,8,8,9]
    },
    {
        'id':12345671,
        'skill':4,
        'points': [8,10,9,9,8,8,9]
    },
    {
        'id':12345671,
        'skill':6,
        'points': [9,10,10,10,8,8,9,9,9]
    },
    {
        'id':12345671,
        'skill':8,
        'points': [9,8,8,10,8,8,9]
    },
    {
        'id':12345671,
        'skill':13,
        'points': [8,10,9,9,8,8,9,10]
    },
    #ERCUMENT
    {
        'id':12345672,
        'skill':4,
        'points': [10,10,7,9,8,8,9,9,7]
    },
    {
        'id':12345672,
        'skill':5,
        'points': [9,9,10,9,8,9,9,7]
    },
    {
        'id':12345672,
        'skill':8,
        'points': [10,8,8,9,9,8,9,9,7]
    },
    {
        'id':12345672,
        'skill':9,
        'points': [8,8,9,10,9,8,9,9,7,9]
    },
    {
        'id':12345672,
        'skill':10,
        'points': [8,8,9,9,10,8,8,9,9,8,9,9,7]
    },
    # HAMDI
    {
        'id': 12345673,
        'skill': 4,
        'points': [9, 10, 9, 9, 8, 8, 9, 9, 7,8,10]
    },
    {
        'id': 12345673,
        'skill': 6,
        'points': [8,8,9, 8, 10, 9, 8, 9, 10,9, 7]
    },
    {
        'id': 12345673,
        'skill': 7,
        'points': [9,9,9,10, 8, 8, 9, 9, 8, 9, 9, 7]
    },
    {
        'id': 12345673,
        'skill': 9,
        'points': [9,9, 8, 9, 10, 9, 8, 9, 9, 7, 9]
    },
    {
        'id': 12345673,
        'skill': 12,
        'points': [7, 8, 9, 9, 10, 9, 9, 8, 9, 9, 7]
    },
    # SELIN
    {
        'id': 21400537,
        'skill': 1,
        'points': [9, 3, 4,7,6,8]
    },
    {
        'id': 21400537,
        'skill': 2,
        'points': [8, 8, 2,6,4]
    },
    {
        'id': 21400537,
        'skill': 3,
        'points': [9, 6,8,7,7,6]
    },
    {
        'id': 21400537,
        'skill': 13,
        'points': [6,7,6,5,5]
    },
    {
        'id': 21400537,
        'skill': 14,
        'points': [7, 8, 6,6,9,5]
    },
    # DOGAN
    {
        'id': 21400538,
        'skill': 1,
        'points': [6,6, 3, 4,7,6,8]
    },
    {
        'id': 21400538,
        'skill': 2,
        'points': [8, 5,8, 2,6,4]
    },
    {
        'id': 21400538,
        'skill': 9,
        'points': [9, 6,9,7,7,6,3]
    },
    {
        'id': 21400538,
        'skill': 13,
        'points': [6,3,6,4,4,10,10]
    },
    {
        'id': 21400538,
        'skill': 14,
        'points': [7, 7, 6,6,9,5,9]
    },
    # CEREN
    {
        'id': 21400539,
        'skill': 1,
        'points': [1, 3, 4,7,6,8]
    },
    {
        'id': 21400539,
        'skill': 2,
        'points': [8, 2, 2,6,4,3]
    },
    {
        'id': 21400539,
        'skill': 9,
        'points': [10, 4,4,8,7,7,6]
    },
    {
        'id': 21400539,
        'skill': 10,
        'points': [2,7,6,5,5,3]
    },
    {
        'id': 21400539,
        'skill': 13,
        'points': [4, 8, 6,6,9,5,4]
    },
    # MAHIR
    {
        'id': 21400540,
        'skill': 1,
        'points': [1, 3, 4,5,5]
    },
    {
        'id': 21400540,
        'skill': 2,
        'points': [5, 8, 2,6,4]
    },
    {
        'id': 21400540,
        'skill': 9,
        'points': [9, 6,7,7,7]
    },
    {
        'id': 21400540,
        'skill': 10,
        'points': [3,7,6,5,5,3]
    },
    {
        'id': 21400540,
        'skill': 14,
        'points': [7, 9, 3,9,5]
    },
    # BERK
    {
        'id': 21400541,
        'skill': 1,
        'points': [2, 3, 4,5,6]
    },
    {
        'id': 21400541,
        'skill': 3,
        'points': [5, 3,6,8, 2,6,4]
    },
    {
        'id': 21400541,
        'skill': 9,
        'points': [9, 6,7,6,5,5]
    },
    {
        'id': 21400541,
        'skill': 10,
        'points': [1,7,6,5,3]
    },
    {
        'id': 21400541,
        'skill': 13,
        'points': [7, 7,4, 3,9,5]
    },
    # SERHAT
    {
        'id': 21400517,
        'skill': 1,
        'points': [5, 3, 6,6,5,8]
    },
    {
        'id': 21400517,
        'skill': 2,
        'points': [5, 4, 2,3,6,4]
    },
    {
        'id': 21400517,
        'skill': 10,
        'points': [9, 6,5,8,6,8]
    },
    {
        'id': 21400517,
        'skill': 13,
        'points': [3,7,2,5,5,4,3]
    },
    # BERAT
    {
        'id': 21400518,
        'skill': 2,
        'points': [5, 3, 6,2,5,2]
    },
    {
        'id': 21400518,
        'skill': 4,
        'points': [5, 4, 5,4]
    },
    {
        'id': 21400518,
        'skill': 6,
        'points': [9, 6,4,6,8]
    },
    {
        'id': 21400518,
        'skill': 9,
        'points': [6,5,5,2,4,3]
    },
    # BAHADIR
    {
        'id': 21400519,
        'skill': 4,
        'points': [6,6,5,9]
    },
    {
        'id': 21400519,
        'skill': 6,
        'points': [5, 7, 6,4]
    },
    {
        'id': 21400519,
        'skill': 9,
        'points': [2, 2,5,3,6,6]
    },
    # TANAY
    {
        'id': 21400527,
        'skill': 2,
        'points': [5, 3, 4,4,4]
    },
    {
        'id': 21400527,
        'skill': 3,
        'points': [5,5,4,7,3,4,3]
    },
    {
        'id': 21400527,
        'skill': 12,
        'points': [4,6,4,3,8,6]
    },
    # FURKAN
    {
        'id': 21400528,
        'skill': 2,
        'points': [7,7,3,5,7]
    },
    {
        'id': 21400528,
        'skill': 7,
        'points': [4,5,6,4,5]
    },
    {
        'id': 21400528,
        'skill': 8,
        'points': [6,6,4,7]
    },
    {
        'id': 21400528,
        'skill': 13,
        'points': [8,8,5,6,6]
    },
    {
        'id': 21400528,
        'skill': 14,
        'points': [3,3,6,5,3]
    },
    # PINAR
    {
        'id': 21400529,
        'skill': 3,
        'points': [4,4,6,5]
    },
    {
        'id': 21400529,
        'skill': 8,
        'points': [8,2,4,6,6]
    },
    {
        'id': 21400529,
        'skill': 10,
        'points': [3,3,7,6,4]
    },
    {
        'id': 21400529,
        'skill': 13,
        'points': [8,4,5,1,6,4]
    },
    # OMER FARUK
    {
        'id': 21400530,
        'skill': 9,
        'points': [6,6,7,3,2]
    },
    {
        'id': 21400530,
        'skill': 11,
        'points': [9,5,7,5,5]
    },
    {
        'id': 21400530,
        'skill': 14,
        'points': [2,2,5,6,4,5,7]
    },
    # BURAK
    {
        'id': 21400531,
        'skill': 10,
        'points': [1,2,3,2,8]
    },
    {
        'id': 21400531,
        'skill': 11,
        'points': [5,5,7,5]
    },
    {
        'id': 21400531,
        'skill': 14,
        'points': [6,6,4,8,4]
    }
])

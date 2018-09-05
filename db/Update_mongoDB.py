from pymongo import MongoClient
from pymongo.errors import ConnectionFailure



a  = ['1','2','3','4','5']


print (a)

a.remove('3')

print (a)

def englam_update():
    try:
        client = MongoClient('localhost', 27017)
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)

    db = client["Amazon_Parse"]

    #result = db.search_status.update({'_id': "1"},{'$inc': {'d.a': 1}},upsert=False,multi=False)
    #result = db.ee.update({'_id': "2"},{'$set': {"name":"englam"}},upsert=False,multi=False)
    #result = db.ee.update_many({'_id': "2"}, {"$set":{"name":"Joseph1","borough":"englam2"}})
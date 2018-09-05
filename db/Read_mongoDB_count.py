from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


try:
    client = MongoClient('localhost', 27017)

except ConnectionFailure as e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)


db = client["Amazon_Parse"]

#read_count = db.Products_Bugs.find().count()

#print (read_count)

cursor = db.Products_Bugs.find()
for i in cursor:
    print (i['bug_title'])
    #print ("bug title:",i['bug_title'])
    #print("bug content:",i['bug_content'])
    #print("feedback author:",i['feedback_author'])
    #print("feedback content:",i['feedback_content'])


'''
bug title: Can't even broadcast half of the wired speed in a ...
bug content: Can't even broadcast half of the wired speed in a two bedroom apartment. Only reason it's not one star is perhaps if you somehow live in a place where there isn't a single other network you can pick up, maybe then it would be adequate. On its way back already.
feedback author: NETGEAR Team

'''
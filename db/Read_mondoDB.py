from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId

try:
    client = MongoClient('localhost', 27017)

except ConnectionFailure as e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)


db = client["Amazon_Parse"]

search_status = db.search_status.find()

print (search_status[0]['status'])

print (search_status[0]['proxy_list']['2'])

print (search_status[0]['query_list'])


#db.products.find({"_id": ObjectId("568c28fffc4be30d44d0398e")})

# "59c7a98eea744412d5d361ce"
print (search_status[0])

search_status2 = db.search_status.find({'_id': '59c7a98eea744412d5d361ce'})





posts = db.posts
post = {"author": "Englam","text": "Englam Text","tags": ["Englam", "python", "pymongo"]}
#post_id = posts.insert_one(post).inserted_id
#print (post_id)

print (posts.find_one())
print (posts.find_one({"author": 'Mike'}))
#print (posts.find_one({"_id": post_id}))
print (posts.find_one({'_id': ObjectId('59c7ba41ea74441d1af0040c')}))


a = list(posts.find({"author": 'Mike'}))
b = list(posts.find({'_id': ObjectId('59c7ba41ea74441d1af0040c')}))

print (a)

print (a[0]['text'])

print (b)



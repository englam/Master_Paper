from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pandas as pd
import numpy as np
import re,string


try:
    client = MongoClient('localhost', 27017)

except ConnectionFailure as e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)


db = client["Amazon_Parse"]

'''print counts'''
read_count = db.Products_Bugs.find().count()
print (read_count)

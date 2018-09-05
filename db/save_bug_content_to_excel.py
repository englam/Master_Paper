from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pandas as pd
import numpy as np
import re,string,xlsxwriter

try:
    client = MongoClient('localhost', 27017)

except ConnectionFailure as e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)


db = client["Amazon_Parse"]

'''print counts'''
#read_count = db.Products_Bugs.find().count()

bug_titls_list          = []
bug_content_list        = []
feedback_content_list   = []
feedback_author_list    = []
model_name_list         = []
price_list              = []
wireless_type_list      = []
bug_date_list           = []
available_date_list     = []

get_Products_Bugs = db.Products_Bugs.find()



for get_Products_Bug in get_Products_Bugs:
    bug_titls_list.append(get_Products_Bug['bug_title'])
    bug_content_list.append(get_Products_Bug['bug_content'])
    feedback_content_list.append(get_Products_Bug['feedback_content'])
    feedback_author_list.append(get_Products_Bug['feedback_author'])
    model_name_list.append(get_Products_Bug['model_name'])
    price_list.append(get_Products_Bug['price'])
    wireless_type_list.append(get_Products_Bug['wireless_type'])
    bug_date_list.append(get_Products_Bug['bug_date'])
    available_date_list.append(get_Products_Bug['available_date'])

'''
print (bug_titls_list[100])
print (bug_content_list[100])
print (feedback_content_list[100])
print (feedback_author_list[100])
print (model_name_list[100])
print (price_list[100])
print (wireless_type_list[100])

print (bug_date_list)

print (available_date_list)
'''


df = pd.DataFrame({'bug_titls_list': bug_titls_list,'bug_content_list':bug_content_list,
                   'feedback_author_list': feedback_author_list,'feedback_content_list':feedback_content_list,
                   'model_name_list': model_name_list,'price_list':price_list,
                   'wireless_type_list':wireless_type_list,'bug_date_list':bug_date_list,'available_date_list':available_date_list
                   },

                  columns=['bug_titls_list', 'bug_content_list', 'feedback_author_list', 'feedback_content_list', 'model_name_list','price_list','wireless_type_list','bug_date_list','available_date_list'])


#df.sort_values('title', ascending=False).to_csv("englam.csv", sep='\t')


#raw_data = {'bug_titls_list': bug_titls_list,'bug_content_list':bug_content_list}

#df = pd.DataFrame(raw_data, columns = ['bug_titls_list', 'bug_content_list'])


#df.to_csv("englam.csv", sep='\t')

#df.to_json('amazon_bugs_3.txt')
#df.to_json('amazon_bugs_3.json')


writer = pd.ExcelWriter('amazon_simple_20180316.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()


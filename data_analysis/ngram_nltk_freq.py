from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pandas as pd
import numpy as np
import re,string
from nltk.corpus import stopwords
from nltk.corpus import swadesh
from nltk import FreqDist

try:
    client = MongoClient('localhost', 27017)

except ConnectionFailure as e:
    sys.stderr.write("Could not connect to MongoDB: %s" % e)
    sys.exit(1)


db = client["Amazon_Parse"]

'''print counts'''
#read_count = db.Products_Bugs.find().count()


get_Products_Bugs = db.Products_Bugs.find()

bug_titls_list          = []
bug_content_list        = []
feedbback_author_list   = []
feedback_content_list   = []

for get_Products_Bug in get_Products_Bugs:
    bug_titls_list.append(get_Products_Bug['bug_title'])
    bug_content_list.append(get_Products_Bug['bug_content'])
    feedbback_author_list.append(get_Products_Bug['feedback_author'])
    feedback_content_list.append(get_Products_Bug['feedback_content'])



#利用nltk的stopwords,把this, a, the ...etc給刪除掉
def content_fraction(text):
    stop_words = stopwords.words('english')
    content = [w for w in text if w.lower() not in stop_words]
    return content


#利用nltk的swadesh,把small,new,because ...etc給刪除掉
def content_fraction2(text):
    compared_words = swadesh.words('en')
    content2 = [w for w in text if w.lower() not in compared_words]
    return content2


#data清理
def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    input = input.upper()
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def getNgrams(input, test_dic, n):
    input = cleanInput(input)
    input = content_fraction(input)
    input = content_fraction2(input)


    for i in range(len(input) - n + 1):
        newNGram = " ".join(input[i:i + n])
        if newNGram in test_dic:
            test_dic[newNGram] += 1
        else:
            test_dic[newNGram] = 1
    return test_dic


def every_content_divided(n,input_list, filename):
    test_dic = dict()
    for bug in input_list:
        if not bool(test_dic):
            ngrams1 = getNgrams(bug, test_dic, n)
            # print (ngrams1)
        else:
            ngrams1 = getNgrams(bug, ngrams1, n)
    return ngrams1



#save_to_file_by_pandas(2,bug_titls_list,"bug_title_1_Gram.csv")



#print (save_to_file_by_pandas(1,bug_content_list[0:1],"test2.csv"))
#print (save_to_file_by_pandas(1,bug_content_list[1:2],"test2.csv"))

for i in range(0,5):
    print(every_content_divided(1, bug_content_list[i:i+1], "test2.csv"))
    print ('')



"""


'''convert bug_titls to 2 gram and save to excel'''
save_to_file_by_pandas(1,bug_titls_list,"bug_title_1_Gram_cleaned.csv")
save_to_file_by_pandas(2,bug_titls_list,"bug_title_2_Gram_cleaned.csv")
save_to_file_by_pandas(3,bug_titls_list,"bug_title_3_Gram_cleaned.csv")
save_to_file_by_pandas(4,bug_titls_list,"bug_title_4_Gram_cleaned.csv")
save_to_file_by_pandas(5,bug_titls_list,"bug_title_5_Gram_cleaned.csv")

'''convert bug_content to 2 gram and save to excel'''
save_to_file_by_pandas(1,bug_content_list,"bug_content_1_Gram_cleaned.csv")
save_to_file_by_pandas(2,bug_content_list,"bug_content_2_Gram_cleaned.csv")
save_to_file_by_pandas(3,bug_content_list,"bug_content_3_Gram_cleaned.csv")
save_to_file_by_pandas(4,bug_content_list,"bug_content_4_Gram_cleaned.csv")
save_to_file_by_pandas(5,bug_content_list,"bug_content_5_Gram_cleaned.csv")

'''convert feedbback_author to 2 gram and save to excel'''
save_to_file_by_pandas(1,feedbback_author_list,"feedbback_author_1_Gram_cleaned.csv")
save_to_file_by_pandas(2,feedbback_author_list,"feedbback_author_2_Gram_cleaned.csv")
save_to_file_by_pandas(3,feedbback_author_list,"feedbback_author_3_Gram_cleaned.csv")
save_to_file_by_pandas(4,feedbback_author_list,"feedbback_author_4_Gram_cleaned.csv")
save_to_file_by_pandas(5,feedbback_author_list,"feedbback_author_5_Gram_cleaned.csv")

'''convert feedback_content to 2 gram and save to excel'''
save_to_file_by_pandas(1,feedback_content_list,"feedback_content_1_Gram_cleaned.csv")
save_to_file_by_pandas(2,feedback_content_list,"feedback_content_2_Gram_cleaned.csv")
save_to_file_by_pandas(3,feedback_content_list,"feedback_content_3_Gram_cleaned.csv")
save_to_file_by_pandas(4,feedback_content_list,"feedback_content_4_Gram_cleaned.csv")
save_to_file_by_pandas(5,feedback_content_list,"feedback_content_5_Gram_cleaned.csv")

"""

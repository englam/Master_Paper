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

    for i in range(len(input) - n + 1):
        newNGram = " ".join(input[i:i + n])
        if newNGram in test_dic:
            test_dic[newNGram] += 1
        else:
            test_dic[newNGram] = 1
    return test_dic


def save_to_file_by_pandas(n,input_list, filename):
    test_dic = dict()
    for bug in input_list:
        if not bool(test_dic):
            ngrams1 = getNgrams(bug, test_dic, n)
            # print (ngrams1)
        else:
            ngrams1 = getNgrams(bug, ngrams1, n)
    content1 = pd.DataFrame(list(ngrams1.items()), columns=['name', 'count'])
    content1.sort_values('count', ascending=False).to_csv(filename, sep='\t')


'''convert bug_titls to 2 gram and save to excel'''
save_to_file_by_pandas(1,bug_titls_list,"bug_title_1_Gram.csv")
save_to_file_by_pandas(2,bug_titls_list,"bug_title_2_Gram.csv")
save_to_file_by_pandas(3,bug_titls_list,"bug_title_3_Gram.csv")
save_to_file_by_pandas(4,bug_titls_list,"bug_title_4_Gram.csv")
save_to_file_by_pandas(5,bug_titls_list,"bug_title_5_Gram.csv")

'''convert bug_content to 2 gram and save to excel'''
save_to_file_by_pandas(1,bug_content_list,"bug_content_1_Gram.csv")
save_to_file_by_pandas(2,bug_content_list,"bug_content_2_Gram.csv")
save_to_file_by_pandas(3,bug_content_list,"bug_content_3_Gram.csv")
save_to_file_by_pandas(4,bug_content_list,"bug_content_4_Gram.csv")
save_to_file_by_pandas(5,bug_content_list,"bug_content_5_Gram.csv")

'''convert feedbback_author to 2 gram and save to excel'''
save_to_file_by_pandas(1,feedbback_author_list,"feedbback_author_1_Gram.csv")
save_to_file_by_pandas(2,feedbback_author_list,"feedbback_author_2_Gram.csv")
save_to_file_by_pandas(3,feedbback_author_list,"feedbback_author_3_Gram.csv")
save_to_file_by_pandas(4,feedbback_author_list,"feedbback_author_4_Gram.csv")
save_to_file_by_pandas(5,feedbback_author_list,"feedbback_author_5_Gram.csv")

'''convert feedback_content to 2 gram and save to excel'''
save_to_file_by_pandas(1,feedback_content_list,"feedback_content_1_Gram.csv")
save_to_file_by_pandas(2,feedback_content_list,"feedback_content_2_Gram.csv")
save_to_file_by_pandas(3,feedback_content_list,"feedback_content_3_Gram.csv")
save_to_file_by_pandas(4,feedback_content_list,"feedback_content_4_Gram.csv")
save_to_file_by_pandas(5,feedback_content_list,"feedback_content_5_Gram.csv")




import sys
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

avail_date = 'August 22, 2016'
bug_time = 'on February 11, 2017'

avail_date = datetime.strptime(avail_date, "%B %d, %Y")

bug_time = bug_time.replace("on ", "")
bug_time = datetime.strptime(bug_time, "%B %d, %Y")

current_date = datetime.now()

def save_to_mongodb(_title, _brand, _model, _price, _wireless_type, _bug_title, _bug_content, _bug_author,
                      _available_date, _bug_date,_feedback_author,_feedback_content,_current_date):

    try:
        client = MongoClient('localhost', 27017)

    except ConnectionFailure as e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    db = client["Amazon_Parse"]

    result =db.Products_Bugs.insert_one(
	    {
	        "title"			: _title,
			"band" 			: _brand,
			"model_name" 	: _model,
			"price" 		: _price,
			"wireless_type" : _wireless_type,
			"bug_title"		: _bug_title,
			"bug_content"	: _bug_content,
			"bug_author"	: _bug_author,
			"feedback_author" : _feedback_author,
			"feedback_content": _feedback_content,
			"bug_date"		: _bug_date,
			"available_date": _available_date,
			"query_date"	: _current_date
	    }
	)

def insert_search_status():
	try:
		client = MongoClient('localhost', 27017)

	except ConnectionFailure as e:
		sys.stderr.write("Could not connect to MongoDB: %s" % e)
		sys.exit(1)
	db = client["Amazon_Parse"]

	result = db.search_status.insert_one(
		{
			"status"		: "locked",
			"query_list"		: [ "111", "222", "333","444"],
			"proxy_list"        : {
				"1": {'host': '208.83.106.105', 'port': 9999},
				"2": {'host': '216.56.48.118', 'port': 9000},
				"3": {'host': '34.232.52.180', 'port': 3128},
				"4": {'host': '198.199.105.118', 'port': 8888},
				"5": {'host': '165.227.124.179', 'port': 3128},
				"6": {'host': '52.33.201.139', 'port': 8083},
				"7": {'host': '40.71.33.56', 'port': 3128},
				"8": {'host': '170.55.15.175', 'port': 3128},
				"9": {'host': '47.91.237.123', 'port': 8080},
				"10": {'host': '174.138.33.157', 'port': 3128},
				"11": {'host': '50.203.117.22', 'port': 80}}


		}
	)

def insert_crawler_name(crawler_name):
	try:
		client = MongoClient('localhost', 27017)

	except ConnectionFailure as e:
		sys.stderr.write("Could not connect to MongoDB: %s" % e)
		sys.exit(1)
	db = client["Amazon_Parse"]

	result = db.crawlers.insert_one(
		{
			"name" 				: crawler_name,
			"status"			: "Empty",
			"query"				: "Empty",
			"brand"				: "Empty",
			"title"				: "Empty",
			"wifi_type"			: "Empty",
			"price"				: "Empty",
			"available_date"	: "Empty",
			"query_url"			: "Empty",
			"running_number"	: "Empty",
			"total_number"		: "Empty",
			"query_time"		: "Empty"

		}
	)


def insert_crawling_history(query,brand,title,wifi_type,price,available_date,query_url,total_number,query_time):
	try:
		client = MongoClient('localhost', 27017)

	except ConnectionFailure as e:
		sys.stderr.write("Could not connect to MongoDB: %s" % e)
		sys.exit(1)
	db = client["Amazon_Parse"]

	result = db.crawling_history.insert_one(
		{
			"query"				: query,
			"brand"				: brand,
			"title"				: title,
			"wifi_type"			: wifi_type,
			"price"				: price,
			"available_date"	: available_date,
			"query_url"			: query_url,
			"total_number"		: total_number,
			"query_time"		: query_time

		}
	)


def insert_log_status():
	try:
		client = MongoClient('localhost', 27017)

	except ConnectionFailure as e:
		sys.stderr.write("Could not connect to MongoDB: %s" % e)
		sys.exit(1)
	db = client["Amazon_Parse"]

	result = db.log_status.insert_one(
		{
			"name"					: "log_status",
			"log_all"				: {},
			"log_captcha"			: {},
			"log_db"				: {},
			"log_error_url_list"	: {},
			"log_error_feedback"	: {},
			"log_url_list"			: {},
		}
	)

def insert_log_crawler(crawler_name):
	try:
		client = MongoClient('localhost', 27017)

	except ConnectionFailure as e:
		sys.stderr.write("Could not connect to MongoDB: %s" % e)
		sys.exit(1)
	db = client["Amazon_Parse"]

	result = db.log_status.insert_one(
		{
			"name"					: crawler_name,
			"log_status"			: {}
		}
	)



if __name__ == "__main__":
	#save_to_mongodb("test","band","model","$145","802.11ac","tttest","13231kfdkjfakdj","keyy",avail_date,bug_time,123,456,current_date)

	#insert_search_status()

	#insert_crawler_name("crawler_1")
	#insert_crawler_name("crawler_3")

	#insert_crawling_history("Netgear R7500v2","Netgear","R7500","802.11a/b/g/n","$1500","2017-09-28 21:57:04.558609","www.amazon.com/r7500v2/test","1000","2017-09-28 21:57:04.558609")

	#insert_log_status()

	#insert_log_crawler("crawler_1")
	insert_log_crawler("crawler_2")
	insert_log_crawler("crawler_3")

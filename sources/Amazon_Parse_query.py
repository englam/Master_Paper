from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId
import datetime, time

class Mongodb_Qquery(object):

    def get_query(self):
        try:
            client = MongoClient('localhost', 27017)

        except ConnectionFailure as e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

        db = client["Amazon_Parse"]

        query_list = db.search_status.find_one({'_id': ObjectId('59c7a98eea744412d5d361ce')})['query_list']

        if len(query_list) is not 0:
            query_parsed = query_list[0]
            query_list.remove(query_parsed)
            db.search_status.update({'_id': ObjectId('59c7a98eea744412d5d361ce')}, {'$set': {'query_list': query_list}})

            print('Query:', query_parsed)
            return (query_parsed)
        return (False)

    def get_proxy(self):
        try:
            client = MongoClient('localhost', 27017)

        except ConnectionFailure as e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

        db = client["Amazon_Parse"]


        proxy_list = db.search_status.find_one({'_id': ObjectId('59c7a98eea744412d5d361ce')})['proxy_list']

        return (proxy_list)

    def get_crawler_info(self,crawler_name):
        try:
            client = MongoClient('localhost', 27017)

        except ConnectionFailure as e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)


        db = client["Amazon_Parse"]

        get_query = db.crawlers.find_one({"name": crawler_name})['query']
        get_title = db.crawlers.find_one({"name": crawler_name})['title']
        get_query_time = db.crawlers.find_one({"name": crawler_name})['query_time']
        get_wifi_type = db.crawlers.find_one({"name": crawler_name})['wifi_type']
        get_price = db.crawlers.find_one({"name": crawler_name})['price']
        get_total_number = db.crawlers.find_one({"name": crawler_name})['total_number']
        get_brand = db.crawlers.find_one({"name": crawler_name})['brand']
        get_status = db.crawlers.find_one({"name": crawler_name})['status']
        get_query_url = db.crawlers.find_one({"name": crawler_name})['query_url']
        get_running_number = db.crawlers.find_one({"name": crawler_name})['running_number']
        get_running_available_date = db.crawlers.find_one({"name": crawler_name})['available_date']

        return (get_query,get_title,get_query_time,get_wifi_type,get_price,get_total_number,get_brand,get_status,get_query_url,get_running_number,get_running_available_date)

    def set_query(self,query_list_set):
        try:
            client = MongoClient('localhost', 27017)

        except ConnectionFailure as e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

        db = client["Amazon_Parse"]

        db.search_status.update({'_id': ObjectId('59c7a98eea744412d5d361ce')}, {'$set': {'query_list': query_list_set}})


    def crawler_status_update(self,crawler_name,mongodb_query,mongodb_title,mongodb_query_time,mongodb_wifi_type,mongodb_price,mongodb_total_number,mongodb_brand,mongodb_status,mongodb_query_url,mongodb_running_number,mongodb_available_date):
        try:
            client = MongoClient('localhost', 27017)
        except ConnectionFailure as e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

        db = client["Amazon_Parse"]

        db.crawlers.update({'name': crawler_name}, {'$set': {'query': mongodb_query}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'title': mongodb_title}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'query_time': mongodb_query_time}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'wifi_type': mongodb_wifi_type}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'price': mongodb_price}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'total_number': mongodb_total_number}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'brand': mongodb_brand}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'status': mongodb_status}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'query_url': mongodb_query_url}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'running_number': mongodb_running_number}})
        db.crawlers.update({'name': crawler_name}, {'$set': {'available_date': mongodb_available_date}})

    def insert_crawling_history(self,query, brand, title, wifi_type, price, available_date, query_url, total_number,query_time):
        try:
            client = MongoClient('localhost', 27017)

        except ConnectionFailure as e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)
        db = client["Amazon_Parse"]

        db.crawling_history.insert_one(
            {
                "query"			    : query,
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




    def insert_log_status(self, log_optional,log_info):
        try:
            client = MongoClient('localhost', 27017)
        except ConnectionFailure as e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

        db = client["Amazon_Parse"]

        if log_optional == "log_db":
            db.log_status.update({'name': 'log_status'}, {
                '$set': {'log_db.' + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%s")): log_info}})

        if log_optional == "log_error_feedback":
            db.log_status.update({'name': 'log_status'}, {
                '$set': {'log_error_feedback.' + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%s")): log_info}})

        if log_optional == "log_error_url_list":
            db.log_status.update({'name': 'log_status'}, {
                '$set': {'log_error_url_list.' + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%s")): log_info}})

        if log_optional == "log_captcha":
            db.log_status.update({'name': 'log_status'}, {
                '$set': {'log_captcha.' + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%s")): log_info}})

        if log_optional == "log_all":
            db.log_status.update({'name': 'log_status'}, {
                '$set': {'log_all.' + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%s")): log_info}})

        if log_optional == "log_url_list":
            db.log_status.update({'name': 'log_status'}, {
                '$set': {'log_url_list.' + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%s")): log_info}})

        print ("Save log")


    def insert_crawler_log_status(self, crawler_name,log_info):
        try:
            client = MongoClient('localhost', 27017)
        except ConnectionFailure as e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

        db = client["Amazon_Parse"]
        db.log_status.update({'name': crawler_name}, {
            '$set': {'log_status.' + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%s")): log_info}})






if __name__ == "__main__":
    crawler_1 = "crawler_1"
    crawler_2 = "crawler_2"
    crawler_3 = "crawler_3"

    #status, running, delete, complete

    mongodb_query_set           = 1
    mongodb_title_set           = 2
    mongodb_query_time_set      = 3
    mongodb_wifi_type_set       = 4
    mongodb_price_set           = 5
    mongodb_total_number_set    = 6
    mongodb_brand_set           = 7
    mongodb_status_set          = 8
    mongodb_query_url_set       = 9
    mongodb_running_number_set  = 10
    mongodb_available_date_set  = 11

    crawler_query_history           = 1
    crawler_brand_history           = 2
    crawler_title_history           = 3
    crawler_wifi_type_history       = 4
    crawler_price_history           = 5
    crawler_available_date_history  = 6
    crawler_query_url_history       = 7
    crawler_total_number_history    = 8
    crawler_query_time_history      = 9


    Searching_Query = Mongodb_Qquery()

    '''get crawler info'''
    #Searching_Query.get_crawler_info(crawler_name)

    '''update crawler'''
    #Searching_Query.crawler_status_update(crawler_1,mongodb_query_set,mongodb_title_set,mongodb_query_time_set,mongodb_wifi_type_set,mongodb_price_set,mongodb_total_number_set,mongodb_brand_set,mongodb_status_set,mongodb_query_url_set,mongodb_running_number_set,mongodb_available_date_set)

    '''insert crawling history'''
    #Searching_Query.insert_crawling_history(crawler_query_history,crawler_brand_history,crawler_title_history,crawler_wifi_type_history,crawler_price_history,crawler_available_date_history,crawler_query_url_history,crawler_total_number_history,crawler_query_time_history)


    '''get query'''
    #print (Searching_Query.get_query())

    '''insert crawler log'''
    #Searching_Query.insert_crawler_log_status(crawler_1,'test1')
    #Searching_Query.insert_crawler_log_status(crawler_2,'test2')
    #Searching_Query.insert_crawler_log_status(crawler_3,'test3')

    '''insert log to log db'''
    #Searching_Query.insert_log_status('log_db','db test2')

    '''insert log to error_feedback_status'''
    #Searching_Query.insert_log_status('log_error_feedback', 'error_feedback_status test2')

    '''insert log to error_url_list'''
    #Searching_Query.insert_log_status('log_error_url_list', 'log_error_url_list test2')

    '''insert log to captcha'''
    #Searching_Query.insert_log_status('log_captcha', 'log_captcha test2')

    '''insert log to log_all'''
    #Searching_Query.insert_log_status('log_all', 'log_all test2')

    '''insert log to log_url_list'''
    Searching_Query.insert_log_status('log_url_list', 'log_url_list test3')

    '''set query list'''
    #query_list_set = ["englam1","englam2","englam3"]
    #Searching_Query.set_query(query_list_set)

# coding=UTF-8
import multiprocessing, random, time
from sources.Amazon_Parse_issue_feedback_v1 import Amazon_Parse
from selenium import webdriver
from datetime import datetime

img_path_1      = 'images/test1.jpg'
img_path_2      = 'images/test2.jpg'
img_path_3      = 'images/test3.jpg'
test_file_1     = 'test1'
test_file_2     = 'test2'
test_file_3     = 'test3'
priority_1      = 'critical'
priority_2      = 'critical'
priority_3      = 'critical'
log_all         = 'log/log_all'
log_one         = 'log/log_one'
log_two         = 'log/log_two'
log_three       = 'log/log_three'

firefox_proxy = 'firefox_proxy'

proxy_list = {
    1: {'host': '208.83.106.105', 'port': 9999},
    2: {'host': '216.56.48.118', 'port': 9000},
    3: {'host': '34.232.52.180', 'port': 3128},
    4: {'host': '198.199.105.118', 'port': 8888},
    5: {'host': '165.227.124.179', 'port': 3128},
    6: {'host': '52.33.201.139', 'port': 8083},
    7: {'host': '40.71.33.56', 'port': 3128},
    8: {'host': '170.55.15.175', 'port': 3128},
    9: {'host': '47.91.237.123', 'port': 8080},
    10: {'host': '174.138.33.157', 'port': 3128},
    11: {'host': '50.203.117.22', 'port': 80}}


def write_log(file_name, message):
    with open(file_name, "a") as f:
        f.write(message + "\n")

def Start_Parse(querys,test_file,_browser,amazon_robot_img,priority,crawler_number,number_log):
    search_url = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="


    for query in querys:
        search_query = search_url+query

        query_log = "[" + str(datetime.now()) + "]" + " Query: " + query
        write_log(log_all, query_log)
        print (query_log)

        random_number = random.randint(1, 11)
        PROXY_HOST = proxy_list[random_number]['host']
        PROXY_PORT = proxy_list[random_number]['port']

        proxy_log = "[" + str(datetime.now()) + "]" + " Proxy: " + str(PROXY_HOST) + ":" + str(PROXY_PORT)
        write_log(log_all, proxy_log)
        print (proxy_log)

        if _browser == 'js':
            amazon_query = Amazon_Parse(webdriver.PhantomJS())

        if _browser == 'firefox':
            amazon_query = Amazon_Parse(webdriver.Firefox())

        if _browser == 'chrome':
            chrome = 'driver/chromedriver'
            amazon_query = Amazon_Parse(webdriver.Chrome(chrome))

        if _browser == 'firefox_proxy':
            fire_path = 'driver/geckodriver'
            profile = webdriver.FirefoxProfile()
            profile.set_preference("network.proxy.type", 1)
            profile.set_preference("network.proxy.http", PROXY_HOST)
            profile.set_preference("network.proxy.http_port", PROXY_PORT)
            amazon_query = Amazon_Parse(webdriver.Firefox(firefox_profile=profile))

        if _browser == 'js_proxy':
            service_args = ['--proxy={}:{}'.format(PROXY_HOST, PROXY_PORT)]
            amazon_query = Amazon_Parse(webdriver.PhantomJS(service_args=service_args))


        amazon_query.amazon_star_clicked(search_query,query,test_file,selected_priority=priority,amazon_robot_img=amazon_robot_img,number_log=number_log)
        amazon_query.close_web()

    print ('[*] Crawling Complete:',crawler_number)



if __name__ == '__main__':

    url             =   "https://www.amazon.com/"
    keyword_1 = ["Netgear WNDR4300","Netgear EX6100","Netgear EX2700","Netgear WNDR3700"]
    keyword_2 = ["Netgear WPN824N","Netgear XAVN2001","Netgear XAVN2001","Netgear R6200v2"]
    keyword_3 = [ "Netgear WNR1000","Netgear A6210","Netgear WNDR3800","Netgear WNDA3100v3"]

    p1 = multiprocessing.Process(target=Start_Parse, args=(keyword_1,test_file_1,firefox_proxy ,img_path_1,priority_1,"Crawler 1",log_one,))
    p2 = multiprocessing.Process(target=Start_Parse, args=(keyword_2,test_file_2,firefox_proxy ,img_path_2,priority_2,"Crawler 2",log_two,))
    p3 = multiprocessing.Process(target=Start_Parse, args=(keyword_3,test_file_3,firefox_proxy ,img_path_3,priority_3,"Crawler 3",log_three,))

    p1.start()
    time.sleep(1)
    p2.start()
    time.sleep(1)
    p3.start()

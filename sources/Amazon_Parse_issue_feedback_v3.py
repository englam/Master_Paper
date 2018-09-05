# coding=UTF-8
# selenium 3.0.2 , firefox 55
# pip install selenium==3.0.2

# pip install selenium==2.53.6


from selenium import webdriver
import time, re, os,multiprocessing,math,sys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from sources.Amazon_Captcha import detect_text
import mysql.connector, random, requests
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from sources.Amazon_Parse_query import Mongodb_Qquery


waiting_time_page = 10
waiting_time_option = 5
waiting_time_robot = 300

log_all         = 'log/log_all'
log_db          = 'log/log_db'
log_feedback    = 'log/log_feedback'
log_captcha     = 'log/log_captcha'
log_error_run   = 'log/log_error_list'
log_urls   = 'log/log_urls_list'

class Amazon_Parse(object):
    def __init__(self, select_webdriver):
        self.driver = select_webdriver
        self.driver.implicitly_wait(30)

    def write_log(self,file_name, message):
        with open(file_name, "a") as f:
            f.write(message + "\n")

    def save_to_mysql(self,_title, _brand, _model, _price, _wireless_type, _bug_title, _bug_content, _bug_author,
                      _available_date, _bug_date,_feedback_author,_feedback_content):
        cnx = mysql.connector.connect(user='root', password='12345678', database='Amazon_Parse_Bugs')
        cursor = cnx.cursor()

        current_date = datetime.now()

        add_bug = ("INSERT INTO demo_test "
                   "(title, brand, model_name, price, wireless_type, bug_title, bug_content, bug_author,query_date,bug_date,available_date,feedback_author,feedback_content) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s,  %s, %s)")

        data = (
        _title, _brand, _model, _price, _wireless_type,  _bug_title, _bug_content, _bug_author, current_date,
        _bug_date, _available_date,_feedback_author,_feedback_content)

        # Insert new employee
        cursor.execute(add_bug, data)

        # Make sure data is committed to the database
        cnx.commit()

        cursor.close()
        cnx.close()

    def save_to_mongodb(self,_title, _brand, _model, _price, _wireless_type, _bug_title, _bug_content, _bug_author,
                        _available_date, _bug_date, _feedback_author, _feedback_content):

        try:
            client = MongoClient('localhost', 27017)

        except ConnectionFailure as e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)
        db = client["Amazon_Parse"]
        current_date = datetime.now()
        result = db.demo_test.insert_one(
            {
                "title"		: _title,
                "band" 			: _brand,
                "model_name" 	: _model,
                "price" 		: _price,
                "wireless_type" : _wireless_type,
                "bug_title"		: _bug_title,
                "bug_content"	: _bug_content,
                "bug_author"	: _bug_author,
                "feedback_author" :_feedback_author,
                "feedback_content": _feedback_content,
                "bug_date"		: _bug_date,
                "available_date": _available_date,
                "query_date"	: current_date,
                "priority"      : "empty"
            }
        )

    def start_search(self,url,query_product):
        self.driver.get(url)
        time.sleep(5)
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(query_product)
        time.sleep(2)
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(Keys.RETURN)
        time.sleep(3)
        bsobj = BeautifulSoup(self.driver.page_source)

        first_url = bsobj.find("", {"id": "result_0"}).find('', {'class': 'a-link-normal a-text-normal'}).attrs['href']
        return (first_url)


    def amazon_star_clicked(self,url,query,test_file,selected_priority,amazon_robot_img,crawler_number):
        try:
            self.driver.get(url)
            time.sleep(waiting_time_page)
            bsobj = BeautifulSoup(self.driver.page_source)
            first_url = bsobj.find("", {"id": "result_0"}).find('', {'class': 'a-link-normal a-text-normal'}).attrs['href']
            time.sleep(2)
            self.driver.get(first_url)
            time.sleep(waiting_time_page)

            bsobj = BeautifulSoup(self.driver.page_source)


            section1_tech = bsobj.find("", {"id": "productDetails_techSpec_section_1"})
            section1_detail = bsobj.find("", {"id": "productDetails_detailBullets_sections1"})
            section2_tech = bsobj.find("", {"id": "productDetails_techSpec_section_2"})
            No_Value = "Empty"


            check_section1_tech = lambda tag: tag.findAll("tr") if tag is not None else No_Value
            check_section1_tech = check_section1_tech(section1_tech)
            check_section1_tech_tr_len = lambda tag: len(tag) if tag is not "Empty" else -1
            check_section1_tech_tr_len = check_section1_tech_tr_len(check_section1_tech)

            check_section1_detail = lambda tag: tag.findAll("tr") if tag is not None else No_Value
            check_section1_detail = check_section1_detail(section1_detail)
            check_section1_detail_tr_len = lambda tag: len(tag) if tag is not "Empty" else -1
            check_section1_detail_tr_len = check_section1_detail_tr_len(check_section1_detail)

            check_section2_tech = lambda tag: tag.findAll("tr") if tag is not None else No_Value
            check_section2_tech = check_section2_tech(section2_tech)
            check_section2_tech_tr_len = lambda tag: len(tag) if tag is not "Empty" else -1
            check_section2_tech_tr_len = check_section2_tech_tr_len(check_section2_tech)


            self.wireless_type = lambda tag: tag.findAll("tr")[0].find("td").text if int(check_section1_tech_tr_len) > 1 else No_Value
            self.wireless_type =self.wireless_type(section1_tech).strip()


            self.brand = lambda tag: tag.findAll("tr")[0].find("td").text if int(check_section2_tech_tr_len) > 1 else No_Value
            self.brand =self.brand(section2_tech).strip()

            self.model_name = lambda tag: tag.findAll("tr")[1].find("td").text if int(check_section2_tech_tr_len) > 1 else No_Value
            self.model_name =self.model_name(section2_tech).strip()

            self.available_date = lambda tag: tag.findAll("tr")[6].find("td").text if int(check_section1_detail_tr_len) > 6 else No_Value
            self.available_date = self.available_date(section1_detail).strip()
            self.available_date = datetime.strptime(self.available_date, "%B %d, %Y")

            self.price = lambda tag: tag.text if tag else No_Value
            self.price = self.price(bsobj.find("", {"id": "priceblock_ourprice"})).strip()

            self.title = bsobj.find("", {"id": "title"}).text
            self.title = self.title.strip()


            #點選星號
            self.driver.find_element_by_xpath('//*[@id="reviewSummary"]/div[1]/a/div/div/div[1]/i/span').click()
            time.sleep(waiting_time_option)

            Check_Initial = True
        except:
            Check_Initial = False
            Initial_log = "[" + str(datetime.now()) + "]" + " Initial Status Error: " + url
            print(Initial_log)

            ''' Save log to log all'''
            Amazon_Parse.write_log(self,log_all,Initial_log)
            Mongodb_Qquery().insert_log_status('log_all', Initial_log)


            ''' Save log to log_error_list'''
            Amazon_Parse.write_log(self, log_error_run , url +',')
            Mongodb_Qquery().insert_crawler_log_status('log_error_url_list', url)

        if Check_Initial:
            Filterted_priority = "[" + str(datetime.now()) + "]" + " Filterted Priority: " + selected_priority
            print(Filterted_priority)

            ''' Save log to log_all'''
            Amazon_Parse.write_log(self, log_all, Filterted_priority)
            Mongodb_Qquery().insert_log_status('log_all', Filterted_priority)

            ''' Save log to number_log'''
            number_log = 'log/log_' + crawler_number
            Amazon_Parse.write_log(self, number_log, Filterted_priority)
            Mongodb_Qquery().insert_crawler_log_status(crawler_number, Filterted_priority)


            Amazon_Parse.get_all_issues(self,query,test_file,amazon_robot_img,selected_priority,crawler_number)

    def amazon_star_filtered(self,option_star):
        time.sleep(2)
        self.driver.find_element_by_id('a-autoid-5-announce').click()
        time.sleep(1)
        Select(self.driver.find_element_by_id('star-count-dropdown')).select_by_visible_text(option_star)
        input('1')
        time.sleep(waiting_time_option)


    def get_current_url(self):
        return (self.driver.current_url)


    def save_to_db(self,product_name,bug_url,crawler_number):

        first_feedback_author = 'Empty'
        first_feedback_content = 'Empty'
        bug_feedback_author = 'Empty'
        bug_feedback_content    = 'Empty'

        try:
            time.sleep(waiting_time_page)
            bsobj = BeautifulSoup(self.driver.page_source)
            '''First Bug'''
            first_title = bsobj.find("", {"class": "a-size-base a-link-normal review-title a-color-base a-text-bold"}).text
            first_content = bsobj.find("", {"class": "a-row review-data"}).text
            first_time = bsobj.find("", {"class": "a-size-base a-color-secondary review-date"}).text
            first_time = first_time.replace("on ", "")
            first_time = datetime.strptime(first_time, "%B %d, %Y")
            first_author = bsobj.find("", {"class": "a-size-base a-link-normal author"}).text

            #for special characters
            first_title_mysql = first_title.encode('ascii', errors='ignore').decode()
            first_content_mysql = first_content.encode('ascii', errors='ignore').decode()
            first_author_mysql = first_author.encode('ascii', errors='ignore').decode()
            first_feedback_author_mysql = first_feedback_author.encode('ascii', errors='ignore').decode()
            first_feedback_content_mysql = first_feedback_content.encode('ascii', errors='ignore').decode()

            #first_feedback_all = bsobj.find("", {"class": "a-section a-spacing-none review-comments"}).text
            if bsobj.find("", {"class": "a-section a-spacing-none review-comments"}).find("", {"class": "a-size-base a-link-normal author"}):
                first_feedback_author = bsobj.find("", {"class": "a-section a-spacing-none review-comments"}).find("", {"class": "a-size-base a-link-normal author"}).text
            if bsobj.find("", {"class": "a-section a-spacing-none review-comments"}).find("", {"class": "a-row a-spacing-top-small"}):
                first_feedback_content = bsobj.find("", {"class": "a-section a-spacing-none review-comments"}).find("", {"class": "a-row a-spacing-top-small"}).text

            #Amazon_Parse.save_to_mysql(self,self.title,self.brand,self.model_name,self.price,self.wireless_type,first_title_mysql,first_content_mysql,first_author_mysql,self.available_date,first_time,first_feedback_author_mysql,first_feedback_content_mysql)
            Amazon_Parse.save_to_mongodb(self,self.title,self.brand,self.model_name,self.price,self.wireless_type,first_title,first_content,first_author,self.available_date,first_time,first_feedback_author,first_feedback_content)

            ''' Save log to log_all'''
            db_success_log = "[" + str(datetime.now()) + "]" + ' Store Issues %s to DB successfully' %(first_title)
            Amazon_Parse.write_log(self, log_all, db_success_log)
            Mongodb_Qquery().insert_log_status('log_all', db_success_log)


            ''' Save log to number_log'''
            Amazon_Parse.write_log(self, crawler_number, db_success_log)
            Mongodb_Qquery().insert_crawler_log_status(crawler_number, db_success_log)

            print (db_success_log)

            time.sleep(1)

            '''Other Bugs except first'''
            for i in bsobj.find("", {"id": "cm_cr-review_list"}).find("", {"class": "a-section review"}).next_siblings:

                if i.find("", {"class": "a-size-base a-link-normal review-title a-color-base a-text-bold"}) is not None:
                    bug_title = i.find("",
                                       {"class": "a-size-base a-link-normal review-title a-color-base a-text-bold"}).text

                    bug_content = i.find("", {"class": "a-row review-data"}).text

                    bug_time = i.find("", {"class": "a-size-base a-color-secondary review-date"}).text
                    bug_time = bug_time.replace("on ", "")
                    bug_time = datetime.strptime(bug_time, "%B %d, %Y")


                    bug_author = i.find("", {"class": "a-size-base a-link-normal author"}).text


                    #bug_feedback_all = i.find("", {"class": "a-section a-spacing-none review-comments"}).text

                    if i.find("", {"class": "a-section a-spacing-none review-comments"}).find("", {"class": "a-size-base a-link-normal author"}):
                        bug_feedback_author = i.find("", {"class": "a-section a-spacing-none review-comments"}).find("", {"class": "a-size-base a-link-normal author"}).text

                    if i.find("", {"class": "a-section a-spacing-none review-comments"}).find("",{"class": "a-row a-spacing-top-small"}):
                        bug_feedback_content = i.find("", {"class": "a-section a-spacing-none review-comments"}).find("",{"class": "a-row a-spacing-top-small"}).text

                    # for special characters
                    bug_title_mysql = bug_title.encode('ascii', errors='ignore').decode()
                    bug_content_mysql = bug_content.encode('ascii', errors='ignore').decode()
                    bug_author_mysql = bug_author.encode('ascii', errors='ignore').decode()
                    bug_feedback_author_mysql = bug_feedback_author.encode('ascii', errors='ignore').decode()
                    bug_feedback_content_mysql = bug_feedback_content.encode('ascii', errors='ignore').decode()


                    #Amazon_Parse.save_to_mysql(self, self.title, self.brand, self.model_name, self.price,self.wireless_type, bug_title_mysql, bug_content_mysql, bug_author_mysql,self.available_date, bug_time, bug_feedback_author_mysql,bug_feedback_content_mysql)

                    Amazon_Parse.save_to_mongodb(self, self.title, self.brand, self.model_name, self.price,
                                               self.wireless_type, bug_title, bug_content, bug_author,
                                               self.available_date, bug_time, bug_feedback_author,
                                               bug_feedback_content)

                    ''' Save log to log_all'''
                    db_success_log_2 = "[" + str(datetime.now()) + "]" + ' Store Issues %s to DB successfully' % (
                        bug_title)
                    Amazon_Parse.write_log(self, log_all, db_success_log_2)
                    Mongodb_Qquery().insert_log_status('log_all', db_success_log_2)

                    ''' Save log to number_log'''
                    Amazon_Parse.write_log(self, crawler_number, db_success_log_2)
                    Mongodb_Qquery().insert_crawler_log_status(crawler_number, db_success_log_2)

                    print(db_success_log_2)


        except:

            product_save_db_error = "[" + str(datetime.now()) + "]" + " product_name: " + product_name + ", Save to DB Error Occures"
            product_error_url = "[" + str(datetime.now()) + "]" + " product_name: " + product_name + ", Error URL , " + bug_url

            print (product_save_db_error)
            print (product_error_url)

            ''' Save log to log_all'''
            Amazon_Parse.write_log(self, log_all , product_save_db_error)
            Amazon_Parse.write_log(self, log_all , product_error_url)
            Mongodb_Qquery().insert_log_status('log_all', product_save_db_error)
            Mongodb_Qquery().insert_log_status('log_all', product_error_url)

            ''' Save log to log_db'''
            Amazon_Parse.write_log(self, log_db , product_save_db_error)
            Amazon_Parse.write_log(self, log_db , product_error_url)
            Mongodb_Qquery().insert_log_status('log_db', product_save_db_error)
            Mongodb_Qquery().insert_log_status('log_db', product_error_url)

            ''' Save log to number_log'''
            Amazon_Parse.write_log(self, crawler_number, product_save_db_error)
            Amazon_Parse.write_log(self, crawler_number, product_error_url)
            Mongodb_Qquery().insert_crawler_log_status(crawler_number, product_save_db_error)
            Mongodb_Qquery().insert_crawler_log_status(crawler_number, product_error_url)

            ''' Save log to log_error_list'''
            Amazon_Parse.write_log(self, log_error_run , bug_url +',')
            Mongodb_Qquery().insert_log_status('log_error_url_list', product_save_db_error)

            time.sleep(waiting_time_robot)



    def save_html_to_file(self,save_file):
        if os.path.isfile(save_file):
            os.remove(save_file)

        time.sleep(2)
        #得到網頁內容
        amazon_content = BeautifulSoup(self.driver.page_source)

        #將網頁內容存下來
        with open(save_file, "a") as f:
            f.write(str(amazon_content) + "\n")

        # 從txt裡面讀取內容
        lines = [line.rstrip('\n') for line in open(save_file)]
        # 過濾讀出來的內容， 將它以 ， 前面<a href=， 後面過濾title方式把url找出來
        customer_ids = [i for i in lines if re.findall(r'comments-for-(.*)">', i)]

        filtered_customer_id_1 = [re.search(r'comments-for-(.*)"><div aria-live', i) for i in customer_ids]
        filtered_customer_id = [filtered_customer_id_1[i].group(1) for i in range(0,len(filtered_customer_id_1))]
        return (filtered_customer_id)



    def Click_Feedback_button(self,customer_id,product_name):
        try:
            for id in customer_id:
                self.driver.find_element_by_xpath('//*[@id="customer_review-%s"]/div[5]/div/a' %(id)).click()
                time.sleep(5)
        except:
            feedback_list = "[" + str(datetime.now()) + "]" + " Click Feedback button Failed: " + str(customer_id)
            print(feedback_list)

            ''' Save log to log_all'''
            Amazon_Parse.write_log(self, log_all, feedback_list)
            Mongodb_Qquery().insert_log_status('log_all', feedback_list)

            ''' Save log to log_feedback'''
            Amazon_Parse.write_log(self, log_feedback, feedback_list)
            Mongodb_Qquery().insert_log_status('log_error_feedback', feedback_list)



    def get_amazon_ai_image(self,img_path, url,crawler_number):
        time.sleep(3)

        a_string = '''Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is accepting cookies.'''

        if a_string in self.driver.page_source:

            if os.path.isfile(img_path):
                os.remove(img_path)

            img = self.driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img')
            src = img.get_attribute('src')

            img = requests.get(src)

            with open(img_path, 'wb') as f:
                f.write(img.content)

            time.sleep(20)
            Captcha_get = "[" + str(datetime.now()) + "]" + " Get Captcha Text "
            print (Captcha_get)

            ''' Save log to log_all'''
            Amazon_Parse.write_log(self, log_all, Captcha_get)
            Mongodb_Qquery().insert_log_status('log_all', Captcha_get)

            ''' Save log to log_captcha'''
            Amazon_Parse.write_log(self, log_captcha, Captcha_get)
            Mongodb_Qquery().insert_log_status('log_captcha', Captcha_get)

            ''' Save log to number_log'''
            Amazon_Parse.write_log(self, crawler_number, Captcha_get)
            Mongodb_Qquery().insert_crawler_log_status(crawler_number, Captcha_get)

            captcha_text = detect_text(img_path, 'AIzaSyBwqm82G8S9ZMAAKgv2-RSosOVQmmgX5Og')

            time.sleep(5)
            Captcha_text_log = "[" + str(datetime.now()) + "]" + " Captcha Text: " + captcha_text
            print (Captcha_text_log)
            ''' Save log to log_all'''
            Amazon_Parse.write_log(self, log_all, Captcha_text_log)
            Mongodb_Qquery().insert_log_status('log_all', Captcha_text_log)

            ''' Save log to log_captcha'''
            Amazon_Parse.write_log(self, log_captcha, Captcha_text_log)
            Mongodb_Qquery().insert_log_status('log_captcha', Captcha_text_log)

            ''' Save log to number_log'''
            Amazon_Parse.write_log(self, crawler_number, Captcha_text_log)
            Mongodb_Qquery().insert_crawler_log_status(crawler_number, Captcha_text_log)


            self.driver.find_element_by_id('captchacharacters').send_keys(captcha_text)
            time.sleep(3)
            self.driver.find_element_by_id('captchacharacters').send_keys(Keys.RETURN)
            #self.driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[2]/div/span/span/button').click()
            time.sleep(3)

            robot_url = "[" + str(datetime.now()) + "]" + " Robot Detection URL: " + url

            ''' Save log to log_all'''
            Amazon_Parse.write_log(self, log_all, robot_url)
            Mongodb_Qquery().insert_log_status('log_all', robot_url)

            ''' Save log to log_captcha'''
            Amazon_Parse.write_log(self, log_captcha, robot_url)
            Mongodb_Qquery().insert_log_status('log_captcha', robot_url)

            ''' Save log to log_captcha'''
            Amazon_Parse.write_log(self, crawler_number, robot_url)
            Mongodb_Qquery().insert_crawler_log_status(crawler_number, robot_url)

        time.sleep(3)


    def get_all_issues(self,product_name,test_file,amazon_robot_img,selected_priority,crawler_number):

        priority_list = {'all': 'all_stars',
                         '5_star': 'five_star',
                         '4_star': 'four_star',
                         '3_star': 'three_star',
                         '2_star': 'two_star',
                         '1_star': 'one_star',
                         'positive': 'positive',
                         'critical': 'critical'}
        current_url = self.get_current_url()


        #for filtered url
        self.driver.get(current_url+'&filterByStar=%s&pageNumber='%(priority_list[selected_priority]) + "1")
        total_bugs = self.driver.find_element_by_xpath('//*[@id="cm_cr-review_list"]/div[1]/span[1]').text
        #total_bugs2 = self.driver.find_element_by_xpath('//*[@id="cm_cr-pagination_bar"]/ul/li[7]/a').text




        total_bugs = total_bugs.replace(total_bugs[0:15], "")
        total_bugs = total_bugs.replace(" reviews", "")
        if "," in total_bugs:
            total_bugs = total_bugs.replace(",", "")


        total_bugs = math.ceil(int(total_bugs) / 10)

        total_bugs_log = "[" + str(datetime.now()) + "]" + " Total_bugs(*10): " + str(total_bugs)
        current_url_log = "[" + str(datetime.now()) + "]" + " Current URL: " + current_url

        ''' Save log to log_all'''
        Amazon_Parse.write_log(self, log_all, total_bugs_log)
        Mongodb_Qquery().insert_log_status('log_all', total_bugs_log)

        ''' Save log to log_all'''
        Amazon_Parse.write_log(self, log_all, current_url_log)
        Mongodb_Qquery().insert_log_status('log_all', current_url_log)

        ''' Save log to number_log'''
        Amazon_Parse.write_log(self, crawler_number, total_bugs_log)
        Mongodb_Qquery().insert_crawler_log_status(crawler_number, total_bugs_log)

        ''' Save log to number_log'''
        Amazon_Parse.write_log(self, crawler_number, current_url_log)
        Mongodb_Qquery().insert_crawler_log_status(crawler_number, current_url_log)

        print(total_bugs_log)
        print(current_url_log)


        for i in range(1, total_bugs + 1):

            bugs_url  = current_url+'&filterByStar=%s&pageNumber='%(priority_list[selected_priority])+ str(i)

            bugs_url_log = "[" + str(datetime.now()) + "]" + " Bugs_url: "+bugs_url
            print (bugs_url_log)

            ''' Save log to log_all'''
            Amazon_Parse.write_log(self, log_all, bugs_url_log)
            Mongodb_Qquery().insert_log_status('log_all', bugs_url_log)

            ''' Save log to log_urls'''
            Amazon_Parse.write_log(self, log_urls, bugs_url_log)
            Mongodb_Qquery().insert_log_status('log_url_list', bugs_url_log)


            ''' Save log to number_log'''
            Amazon_Parse.write_log(self, crawler_number, bugs_url_log)
            Mongodb_Qquery().insert_crawler_log_status(crawler_number, bugs_url_log)


            # start crawling
            print("[" + str(datetime.now()) + "]" + " Start Crawling ")
            self.driver.get(bugs_url)

            # check amazon crawling detection
            self.get_amazon_ai_image(amazon_robot_img, bugs_url,crawler_number)

            time.sleep(waiting_time_page)
            feedback_id = self.save_html_to_file(test_file)
            self.Click_Feedback_button(feedback_id,product_name)
            self.save_to_db(product_name,bugs_url,crawler_number)


    def close_web(self):
        self.driver.close()
        self.driver.quit()


def Start_Parse(querys,test_file,_browser,amazon_robot_img,crawler_number):
    search_url = "https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="

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

    #priorities = ['3 star only','2 star only','1 star only']
    priorities = ['critical']

    for query in querys:
        search_query = search_url+query
        print ("[*] Keyword Query:",query)

        for priority in priorities:

            random_number = random.randint(1, 11)
            print('[*] Random Number: ', random_number)
            PROXY_HOST = proxy_list[random_number]['host']
            PROXY_PORT = proxy_list[random_number]['port']

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




            #從URL點擊星號



            amazon_query.amazon_star_clicked(search_query,query,test_file,selected_priority=priority,amazon_robot_img=amazon_robot_img,crawler_number=crawler_number)



            amazon_query.close_web()





if __name__ == '__main__':
    crawler_1 = "crawler_1"
    crawler_2 = "crawler_2"
    crawler_3 = "crawler_3"
    Searching_Query = Mongodb_Qquery()

    '''get crawler info'''
    crawler_1_status = Searching_Query.get_crawler_info(crawler_1)[7]
    crawler_2_status = Searching_Query.get_crawler_info(crawler_2)[7]
    crawler_3_status = Searching_Query.get_crawler_info(crawler_3)[7]

    keyword_1 = ["NETGEAR R9000"]


    p1 = multiprocessing.Process(target=Start_Parse, args=(keyword_1, "test1", 'firefox_proxy', 'test1.jpg','crawler_1',))
    p1.start()



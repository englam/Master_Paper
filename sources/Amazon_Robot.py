
from selenium import webdriver
from bs4 import BeautifulSoup
from sources.Amazon_Captcha import detect_text
#from Amazon_Captcha import detect_text
import requests, time


def get_amazon_ai_image(img_file,url):
    img_path = '../images/' + img_file

    driver = webdriver.Firefox()
    driver.get(url)

    time.sleep(3)

    bsobj = BeautifulSoup(driver.page_source)

    a_string = '''Sorry, we just need to make sure you're not a robot. For best results, please make sure your browser is accepting cookies.'''

    print ('[*] Check Robot String')
    if a_string in bsobj:

        img = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img')
        src = img.get_attribute('src')

        img = requests.get(src)
        print('[*] Save Image')
        with open(img_path, 'wb') as f:
            f.write(img.content)

        print('[*] Get Captcha Text')
        captcha_text = detect_text(img_path, 'AIzaSyBwqm82G8S9ZMAAKgv2-RSosOVQmmgX5Og')
        time.sleep(5)
        print('[*] Send Captcha Key')
        driver.find_element_by_id('captchacharacters').send_keys(captcha_text)
    else:
        print('[*] Return Process')

    time.sleep(3)
    driver.close()
    driver.quit()


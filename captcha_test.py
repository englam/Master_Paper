from selenium import webdriver
import time, requests
from sources.Amazon_Captcha import detect_text
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://www.amazon.com/errors/validateCaptcha?amzn=mmPwQAw1oQjxhunppfyiSA%3D%3D&amzn-r=%2F&field-keywords=')

img = driver.find_element_by_xpath('/html/body/div/div[1]/div[3]/div/div/form/div[1]/div/div/div[1]/img')
src = img.get_attribute('src')

img = requests.get(src)

with open('images/test4.jpg', 'wb') as f:
    f.write(img.content)

time.sleep(10)
captcha_text = detect_text('images/test4.jpg', 'AIzaSyBwqm82G8S9ZMAAKgv2-RSosOVQmmgX5Og')

print (captcha_text)

driver.find_element_by_xpath('//*[@id="captchacharacters"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="captchacharacters"]').send_keys(captcha_text)
#driver.find_element_by_id('captchacharacters').send_keys(captcha_text)
time.sleep(3)
#driver.find_element_by_id('captchacharacters').send_keys(Keys.RETURN)

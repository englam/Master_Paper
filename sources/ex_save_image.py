from selenium import webdriver
import time, requests

#如果原圖是jpg 那下載的要用jpg, 如果原圖是png,那下載要用png

driver = webdriver.Firefox()
driver.get("https://www.python.org/")
time.sleep(10)

img = driver.find_element_by_xpath('//*[@id="touchnav-wrapper"]/header/div/h1/a/img')
src = img.get_attribute('src')


img = requests.get(src)
with open('../images/captcha.png', 'wb') as f:
    f.write(img.content)

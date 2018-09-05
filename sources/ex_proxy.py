from selenium import webdriver
from selenium.webdriver.common.proxy import *






#PROXY_HOST = '208.83.106.105'
#PROXY_PORT = 9999

#PROXY_HOST = '216.56.48.118'
#PROXY_PORT = 9000


#PROXY_HOST = '34.232.52.180'
#PROXY_PORT = 3128

#PROXY_HOST = '198.199.105.118'
#PROXY_PORT = 8888


#PROXY_HOST = '165.227.124.179'
#PROXY_PORT = 3128

#PROXY_HOST = '52.33.201.139'
#PROXY_PORT = 8083

#PROXY_HOST = '40.71.33.56'
#PROXY_PORT = 3128

#PROXY_HOST = '170.55.15.175'
#PROXY_PORT = 3128

#PROXY_HOST = '47.91.237.123'
#PROXY_PORT = 8080

#PROXY_HOST = '174.138.33.157'
#PROXY_PORT = 3128

PROXY_HOST = '50.203.117.22'
PROXY_PORT = 80

profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", PROXY_HOST)
profile.set_preference("network.proxy.http_port", PROXY_PORT)
#profile.set_preference("network.proxy.socks_username", "405085087")
#profile.set_preference("network.proxy.socks_password", "Kk882246821")
profile.update_preferences()

# executable_path  = define the path if u don't already have in the PATH system variable.


#browser = webdriver.Firefox(firefox_profile=profile)
#browser.get("http://icanhazip.com")
#browser.close()

proxyIP = '50.203.117.22'
proxyPort = '80'
service_args = [
    #'--proxy=174.138.33.157:3128'
    '--proxy={}:{}'.format(proxyIP, proxyPort)
    ]

browser = webdriver.PhantomJS(service_args=service_args)
browser.get("http://icanhazip.com")
print (browser.page_source)
browser.close()


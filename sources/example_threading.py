

import socket, json, time, os, shutil,threading, sys, logging
from datetime import datetime




class Central_Controler(threading.Thread):
    def __init__(self):
        self._running = True
        self.startup =""

    def terminate(self):
        self._running = False

    def Packets_Received(self,url):
        print(url)
        englam(url)



def englam(url):
    print(url,"englam")

def test(url):
    print (url,"test")



if __name__ == '__main__':
    url = 'http://www.yahoo.com.tw'
    url2 = 'http://www.amazon.com.tw'
    Control         = Central_Controler()
    e1        = threading.Thread(target=Control.Packets_Received, args=(url,))
    e2        = threading.Thread(target=Control.Packets_Received, args=(url2,))

    e1.start()
    e2.start()
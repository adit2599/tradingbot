#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'notebook')
import requests
from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from xlrd import open_workbook
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime as datetime
def zerodha_login():
    #file=open(r'credentials.txt','r')
    #det=file.read().split('\n')
    USERID=abcd
    Password=efgh
    Pin=fghi
    browser.get('https://kite.zerodha.com/chart/web/ciq/NSE/INFRATEL/7458561')
    user=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[2]/input')
    passw=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[3]/input')
    user.send_keys(USERID)
    passw.send_keys(Password)
    login=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[4]/button')
    login.click()
    time.sleep(1)
    PIN=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[2]/div/input')
    PIN.send_keys(Pin)
    Continue=browser.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div/div/div/form/div[3]/button')
    Continue.click()


Channel='12345678'#Channel Id of our bot
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2
})
browser = webdriver.Chrome(options=option, executable_path='/Users/adit.25/Desktop/chromedriver')

zerodha_login()

time.sleep(2)

section5=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/ul/li[5]')
section5.click()

time.sleep(2)

p1=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/div/div/span[2]/span[3]')

p2=browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/div/span[2]/span[3]')


bought_at=187.3
stoploss=1.1*bought_at


while(True):
    t1 = time.perf_counter()
    val=float(p1.text)+float(p2.text)
    
    if(val>=stoploss):
        time_now = str(datetime.datetime.now()).split(' ')[1].split('.')[0]
        message = '{} STOPLOSS HIT!: [CE: {} PE:{}]'.format(time_now, p1.text, p2.text)
        print(message)
        # sendTelegramMsg(message)
        
    t2 = time.perf_counter()
    try:
        time.sleep(np.around(1 - (t2 - t1))) #Scan again after 1 sec
    except KeyboardInterrupt:
        print('KeyboardInterrupt. Exiting.')
        break
    except:
        pass


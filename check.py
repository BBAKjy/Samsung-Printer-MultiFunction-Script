# pip install bs4
# pip install selenium
# pip install pyautogui
# need Chrome Web Driver

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os
import pyautogui
import time

import time

f = open("ips.txt", 'r')
ips = f.readlines()

# Need Change
#ips = ['113.10.140.240\n', '113.0.238.21\n', '113.0.238.29\n', '113.0.238.45\n', '113.0.126.182\n', '113.0.211.140\n', '113.0.212.76\n', '113.0.217.36\n', '113.0.223.42\n', '113.0.231.231\n', '113.0.231.26\n', '113.0.233.30\n', '113.0.237.31\n', '113.0.238.26\n', '113.0.34.30\n', '113.0.35.189\n', '113.10.95.43\n', '113.0.237.24\n', '113.0.237.27\n', '113.0.237.50\n', '113.10.141.23\n', '113.0.72.105\n', '113.0.72.26\n', '113.0.72.86\n', '113.0.72.92\n', '113.0.66.106\n', '113.0.66.24\n', '113.0.66.32\n', '113.0.66.33\n', '113.0.66.50\n', '113.10.94.32\n', '113.0.212.100\n', '113.0.212.122\n', '113.10.94.115\n', '113.10.70.61\n', '113.10.200.21\n', '113.10.132.134\n', '113.10.140.67\n', '113.0.232.103\n', '113.0.232.128\n', '113.0.232.140\n', '113.0.232.200\n', '113.0.232.201\n', '113.0.234.10\n', '113.0.234.133\n', '113.0.234.63\n', '113.0.234.73\n', '113.0.234.87\n', '113.0.234.88\n', '113.10.10.39\n', '113.10.10.40\n', '113.10.155.13\n', '113.10.151.154\n', '113.10.151.47\n', '113.10.151.63\n', '113.10.151.84\n', '113.0.121.118\n', '113.0.73.37\n', '113.20.10.164\n', '113.20.49.239\n', '113.20.49.53\n', '113.20.65.98\n', '113.0.35.207\n', '113.0.35.209\n', '113.0.35.211\n', '113.0.35.213\n', '113.0.35.31\n', '113.0.35.32\n', '113.0.13.44\n', '113.0.13.46\n', '113.0.13.48\n', '113.0.13.56\n', '113.0.223.27']

for ip in ips:
    try:
        time.sleep(1)
        ip = ip[0:-1]
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        #options.add_argument('headless') # Headless Mode -> Don't run Web Browser

        driver = webdriver.Chrome('chromedriver.exe', options=options) # Chrome Driver Path


        #driver.set_window_size(1920, 1200)
        driver.implicitly_wait(10)
        driver.get("http://" + ip) # Reqeust to Target using GET Method
        driver.maximize_window()
        #driver.save_screenshot(ip + '_01.png')

        time.sleep(5)

        driver.find_element_by_id('ext-gen211').click()

        # ID PASSWORD NEED CAHGNE
        driver.find_element_by_id('XXI_LOGIN_IN').send_keys('admin')
        driver.find_element_by_id('XXI_LOGIN_PASSWORD').send_keys('sec00000')
        driver.find_element_by_id('XXI_LOGIN_BTN').click()

        time.sleep(10)

        # OUTPUT FILE NAME NEED CHANGE
        im1 = pyautogui.screenshot(ip + "_03.png", region=(0,0,1294,765))

        driver.quit()

    except Exception as e:
        k = open('except2.txt', 'a')
        k.write(ip + "     " + str(e) + "\n")
        k.close()
        continue



# f = open("ip.txt", 'r')
# u = f.readlines()

# for i in range(len(u)):
#     options = webdriver.ChromeOptions()
#     options.add_argument('headless') # Headless Mode -> Don't run Web Browser

#     driver = webdriver.Chrome('C:\\Users\\pijy0\\Documents\\chromedriver.exe', options=options) # Chrome Driver Path

#     driver.get("192.168.1.52") # Reqeust to Target using GET Method

#     driver.save_screenshot('a.png')

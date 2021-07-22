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

tempIPS = ["113.10.132.153"]

try:
    f = open("ips.txt", 'r')
    ips = f.readlines()

    if len(ips) == 0:
        ips = tempIPS

except:
    # Need Change
    ips = tempIPS

print(ips)


# for ip in ips:
#     try:
#         time.sleep(1)
#         ip = ip[0:-1]
#         options = webdriver.ChromeOptions()
#         options.add_argument("--incognito")
#         options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         options.add_experimental_option("excludeSwitches", ["enable-logging"])
#         options.add_experimental_option('useAutomationExtension', False)
#         #options.add_argument('headless') # Headless Mode -> Don't run Web Browser

#         driver = webdriver.Chrome('chromedriver.exe', options=options) # Chrome Driver Path


#         #driver.set_window_size(1920, 1200)
#         driver.implicitly_wait(10)
#         driver.get("http://" + ip) # Reqeust to Target using GET Method
#         driver.maximize_window()
#         #driver.save_screenshot(ip + '_01.png')

#         time.sleep(5)

#         try:
#             driver.find_element_by_id('ext-gen211').click()
#         except:
#             driver.find_element_by_id('ext-gen202').click()

#         # ID PASSWORD NEED CAHGNE
#         driver.find_element_by_id('XXI_LOGIN_IN').send_keys('admin')
#         driver.find_element_by_id('XXI_LOGIN_PASSWORD').send_keys('sec00000')
#         driver.find_element_by_id('XXI_LOGIN_BTN').click()

#         time.sleep(10)

#         # OUTPUT FILE NAME NEED CHANGE
#         im1 = pyautogui.screenshot(ip + "_03.png", region=(0,0,1294,765))

#         driver.quit()

#     except Exception as e:
#         k = open('except2.txt', 'a')
#         k.write(ip + "     " + str(e) + "\n")
#         k.close()
#         continue

# ====================================================================================================
# 80포트 확인

for ip in ips:
    try:
        time.sleep(1)
        ip = ip[0:-1]
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        #options.add_argument('headless') # Headless Mode -> Don't run Web Browser

        driver = webdriver.Chrome('chromedriver.exe', options=options) # Chrome Driver Path


        #driver.set_window_size(1920, 1200)
        driver.implicitly_wait(10)
        driver.get("http://" + ip) # Reqeust to Target using GET Method
        driver.maximize_window()
        #driver.save_screenshot(ip + '_01.png')

        time.sleep(5)

        # OUTPUT FILE NAME NEED CHANGE
        im1 = pyautogui.screenshot(ip + "_01.png", region=(0,0,1294,765))

        driver.quit()

    except Exception as e:
        k = open('except1.txt', 'a')
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
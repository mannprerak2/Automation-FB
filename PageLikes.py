# coding: utf-8


#PreRequisites-
    #Be sure to change chrome driver path in get driver function (line 37)
    #use python3
    #install selenium for python3
    
# structure of this file-----
    # 1) imports
    # 2) gloabal variables
    # 3) functions
    # 4) code
    # 5) algo or how to...(complex stuff only)



#imports------start
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass
#imports-------end



#global variables----------start
email_str = ""
pass_str = ""
driver = webdriver
#global variables----------end



#functions---------start
def askLoginDetails():
    global email_str,pass_str
    email_str = input("Enter fb email > ")
    pass_str = getpass.getpass("Enter password >")

def getDriver():
    global driver
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(
        # executable_path="/home/prerak/AnacondaProjects/chromedriver",chrome_options=chrome_options) - Prerak
        # executable_path='/Users/Batman/anaconda/chromedriver',chrome_options=chrome_options) - Aman
        # executable_path="/usr/bin/chromedriver",chrome_options=chrome_options) - Saurabh
    #change this acc to driver location in ur pc

def openFB():
    driver.get("https://www.facebook.com/")

def loginToFB():
    emailbox = driver.find_element_by_css_selector("input[type='email']")
    emailbox.send_keys(email_str)#enter email
    passbox = driver.find_element_by_css_selector("input[type='password']")
    passbox.send_keys(pass_str)#enter password
    passbox.send_keys(Keys.RETURN)

def visitPage():
    driver.get("https://www.facebook.com/pg/YourEdm/posts/")

def likePost():
    cancel = driver.find_element_by_css_selector("a[action='cancel']")  #manually exiting the notification pop-up
    cancel.click()
    
    like = driver.find_elements_by_css_selector("a[role='button'][href='#'][tabindex='0']")
    time.sleep(3)  
    for i in range(len(like)):
        if (like[i].get_attribute('text') == 'Like'):
            like[i].click()
#functions---------end



#code logic-------start
askLoginDetails()
getDriver()
openFB()
loginToFB()
visitPage()
likePost()
#code logic-------end



#algo --------start
'''




'''
#algo---------end


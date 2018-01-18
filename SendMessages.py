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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
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
    email_str = input("Enter facebook e-mail > ")
    pass_str = getpass.getpass("Enter password >")

def getDriver():
    global driver
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    #driver = webdriver.Chrome(executable_path='/Users/Batman/anaconda3/chromedriver',chrome_options=chrome_options)#amandeep
    driver = webdriver.Chrome(executable_path="/home/prerak/AnacondaProjects/chromedriver",chrome_options=chrome_options)#prerak
    #driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options) #saurabh
    #change this acc to driver location in ur pc

def openFB():
    driver.get("https://www.facebook.com/")

def loginToFB():
    global email_str,pass_str
    emailbox = driver.find_element_by_css_selector("input[type='email']")
    emailbox.send_keys(email_str)#enter email
    passbox = driver.find_element_by_css_selector("input[type='password']")
    passbox.send_keys(pass_str)#enter password
    passbox.send_keys(Keys.RETURN)

def check_id():
    time.sleep(3)
    try:
        driver.find_element_by_id("email")
        print("Incorrect ID or Password. Please try again.")
        exit(0)

    except NoSuchElementException:
        return True

def login():
        loginToFB()
        check_id()

def OpenMessageBox():
    global driver
    action1 = ActionChains(driver)
    time.sleep(2)
    action1.key_down(Keys.ALT)
    action1.key_down(Keys.SHIFT)
    action1.send_keys("m")
    action1.key_up(Keys.ALT)
    action1.key_up(Keys.SHIFT)
    action1.perform()
    print("Pressed")
    time.sleep(0.5)


def sendName():
    global driver
    action2 = ActionChains(driver)
    action2.send_keys("prerak mann")
    time.sleep(2)
    action2.send_keys(Keys.ENTER).perform()

    action3 = ActionChains(driver)
    action3.send_keys("anirudh gupta")
    time.sleep(2)
    action3.send_keys(Keys.ENTER).perform()
    time.sleep(2)

    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)
    ActionChains(driver).send_keys(Keys.TAB).perform()
    time.sleep(1)


    action5 = ActionChains(driver)
    action5.send_keys("hi bro kaisa hai? dont reply back,purani id hai ye")
    action5.send_keys(Keys.ENTER)
    action5.perform()


#functions---------end



#code logic-------start
askLoginDetails()
getDriver()
openFB()
login()
OpenMessageBox()
sendName()
#code logic-------end



#algo --------start
'''




'''
#algo---------end

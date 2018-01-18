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
    # driver = webdriver.Chrome(executable_path="/home/prerak/AnacondaProjects/chromedriver",chrome_options=chrome_options)#prerak
    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options) #saurabh
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
        # exit(0)
        driver.close()
        
    except NoSuchElementException:
        return True

def login():
        loginToFB()
        check_id()
        
def visitPage():
    pageName = "https://www.facebook.com/pg/YourEdm/posts/"
    print("Visiting ->",pageName) 
    driver.get(pageName)


def likePost():
    #cancel = driver.find_element_by_css_selector("a[action='cancel']")  #manually exiting the notification pop-up
    #cancel.click()  # not required as we use icognito 
    counter = 0
    last_height = 0
    i=0

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        like = driver.find_elements_by_css_selector("a[data-testid='fb-ufi-likelink'][tabindex='0']")
        for index in range(len(like)):
            if (like[index].is_displayed()):
                if (like[index].get_attribute('clientWidth') > 0):
                    like[index].click()
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break
        
        last_height = new_height
        i+=1
        
        if (i>10):
            break
#functions---------end



#code logic-------start
askLoginDetails()
getDriver()
openFB()
login()
visitPage()
likePost()
#code logic-------end



#algo --------start
'''




'''
#algo---------end


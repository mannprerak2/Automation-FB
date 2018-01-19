# coding: utf-8


#PreRequisites-
    #Be sure to change chrome driver path in get driver function (line 37)
    #Use python3
    #Install selenium for python3
    
# Structure of this file-----
    # 1) imports
    # 2) gloabal variables
    # 3) functions
    # 4) code
    # 5) algo or how to...(complex stuff only)



#imports------start
import selenium
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

#imports-------end


#global variables----------start
email_str = ""
pass_str = ""
pageName = ""
likes=0
driver = webdriver
#global variables----------end


#functions---------start
def getDriver():
    global driver
    
    chrome_options=webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(executable_path='/Users/Batman/anaconda3/chromedriver',chrome_options=chrome_options)            #amandeep
    #driver = webdriver.Chrome(executable_path="/home/prerak/AnacondaProjects/chromedriver",chrome_options=chrome_options)     #prerak
    #driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=chrome_options)                            #saurabh
    
    #change this acc to driver location in ur pc

def askLoginDetails():
    global email_str,pass_str,pageName,likes
    email_str = input("Enter Facebook e-mail or username > ")
    pass_str = getpass.getpass("Enter password >")    
    pageName = input("Enter the page link >")
    likes= input("Enter number of posts to be liked(Enter 0 to like all possible posts) >")
    likes=int(likes)
    
def openFB():
    driver.get("https://www.facebook.com/")

def loginToFB():
    global email_str,pass_str

    emailbox = driver.find_element_by_css_selector("input[type='email']")
    emailbox.send_keys(email_str)                                            #enter email
    passbox = driver.find_element_by_css_selector("input[type='password']")
    passbox.send_keys(pass_str)                                              #enter password
    passbox.send_keys(Keys.RETURN)

def check_id():
    time.sleep(3)
    try:
        driver.find_element_by_id("email")
        print("Incorrect ID or Password. Please try again.")
        driver.close()
        exit(0)
        
    except NoSuchElementException:
        return True

def visitPage():
    global pageName
    pageName = pageName + 'posts'
    print("Visiting ->",pageName) 
    driver.get(pageName)

def likePost():
    counter = 0
    last_height = 0
    i=0

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        like = driver.find_elements_by_css_selector("a[data-testid='fb-ufi-likelink'][tabindex='0']")
        for index in range(len(like)):
            if (like[index].is_displayed()):
                if (int(like[index].get_attribute('clientWidth')) > 0):
                    driver.execute_script("arguments[0].click();",like[index])
                    counter+=1
            if likes>0 and likes==counter:
                return

        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            break

        last_height = new_height


    print (str(counter) + " posts liked.")

def login():
        loginToFB()
        check_id()
        
#functions---------end


#code logic-------start
askLoginDetails()
getDriver()
openFB()
login()
visitPage()
likePost()
driver.close()
#code logic-------end



#algo --------start
'''




'''
#algo---------end


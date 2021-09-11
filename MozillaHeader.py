from selenium import webdriver
import os
import selenium #maybe just use keybinds instead of parsing the whole fking document lol
#from ui.css import Ui_Dialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains #https://stackoverflow.com/questions/49477856/why-am-i-getting-nameerror-name-actionchains-is-not-defined #https://www.geeksforgeeks.org/action-chains-in-selenium-python/
from selenium.common.exceptions import NoSuchElementException
import cryptography
from cryptography.fernet import Fernet
import sqlite3
from bs4 import BeautifulSoup
import re
import os
import importlib
#from locate_xpath import Xpath_Util
#from githubMain import login
import time
from time import sleep
from encryptiondata import EncryptionData
#EncryptionDataInstance = EncryptionData()
#EncryptionDataInstance.getactiveAccounts(); print('chromeheader active accounts:'); print(EncryptionData.activeAccounts)

class MozillaHeader():
    def __init__(self, **kwargs):
        super(ChromeHeader, self).__init__(**kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        #driver = webdriver.Remote(service.service_url,   desired_capabilities=chrome_options.to_capabilities())
        ChromeHeader.MyBrowserInstance = webdriver.Chrome() 
        driver = ChromeHeader.MyBrowserInstance
        ChromeHeader.url = driver.command_executor._url; print(ChromeHeader.url)
        ChromeHeader.session_id = driver.session_id; print(ChromeHeader.session_id) #https://duckduckgo.com/?t=ffab&q=connecting+to+an+active+webdriver+instace+python&atb=v1-1&ia=web&iax=qa
        #driver = ChromeHeader.webdriver.Remote(command_executor=ChromeHeader.url,desired_capabilities={}) #https://duckduckgo.com/?t=ffab&q=connecting+to+an+active+webdriver+instace+python&atb=v1-1&ia=web&iax=qa
        print(driver.session_id) #https://github.com/SeleniumHQ/selenium/issues/915
        #selenium.webdriver.chrome.webdriver.WebDriver (session="c61348f5f749b9e64dda71407e7154f0")
        driver.close()
        #print(ChromeHeader.__dict__)
        #print(vars(ChromeHeader))
        #print(ChromeHeader.MyBrowserInstance)
        #url = ChromeHeader.MyBrowserInstance.command_executor._url
        #session_id = ChromeHeader.MyBrowserInstance.session_id

    def CloseDriver():
        #global ChromeHeader.MyBrowserInstance
        ChromeHeader.MyBrowserInstance.quit()

#def remoteconn():
#
#ChromeHeader()
"""
Qxf2 Services: Utility script to generate XPaths for the given URL
https://qxf2.com/blog/auto-generate-xpaths-using-python/
https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f
"""
class FailedLogin(BaseException):
    pass #https://www.programiz.com/python-programming/user-defined-exception
#instance = ChromeHeader()
#class classproxy():
#https://duckduckgo.com/?t=ffab&q=list+all+attributes+of+an+object+using+python&atb=v1-1&ia=web
class Xpath_Util(EncryptionData, FailedLogin): #login, #ChromeHeader,  
    "Class to generate the xpaths"
 
    def __init__(self, **kwargs):
        super(Xpath_Util, self).__init__(**kwargs)
        #super(self, Xpath_Util).__init__(**kwargs)
        "Initialize the required variables"
        self.elements = None
        self.guessable_elements = ['input','button']
        self.known_attribute_list = ['id','name','placeholder','value','title','type','class']
        self.variable_names = []
        self.button_text_lists = []
        self.mypaths = []
        self.language_counter = 1
        #url = ChromeHeader.url
        #driver = webdriver.Remote(command_executor=url,desired_capabilities={}) #https://duckduckgo.com/?t=ffab&q=connecting+to+an+active+webdriver+instace+python&atb=v1-1&ia=web&iax=qa
        #driver.session_id = ChromeHeader.session_id
        #driver = ChromeHeader.webdriver.remote(ChromeHeader.session_id)
        #print()

    def generate_xpath(self, soup):
        "generate the xpath and assign the variable names"
        result_flag = False
        #xpath_obj = chromeHeader.xpath_obj
        #driver = ChromeHeader.MyBrowserInstance
        for guessable_element in self.guessable_elements:
            self.elements = soup.find_all(guessable_element)
            for element in self.elements:
                if (not element.has_attr("type")) or (element.has_attr("type") and element['type'] != "hidden"):
                    for attr in self.known_attribute_list:
                        if element.has_attr(attr):
                            locator = self.guess_xpath(guessable_element,attr,element)
                            if len(driver.find_elements_by_xpath(locator))==1: #ChromeHeader.MyBrowserInstance
                                result_flag = True
                                variable_name = self.get_variable_names(element)
                                # checking for the unique variable names
                                if  variable_name != '' and variable_name not in self.variable_names:
                                    self.variable_names.append(variable_name)
                                    #mypaths = [] 
                                    #self.mypaths.append("%s_%s = %s"%(guessable_element, variable_name.encode('utf-8').decode('latin-1'), locator.encode('utf-8').decode('latin-1')))
                                    self.mypaths.append("%s"%(locator.encode('utf-8').decode('latin-1')))
                                    print(self.mypaths)
                                    #print('element printed')
                                    break
                                else:
                                    print (locator.encode('utf-8').decode('latin-1') + "----> Couldn't generate appropriate variable name for this xpath")
                        elif guessable_element == 'button' and element.getText():
                            button_text = element.getText()
                            if element.getText() == button_text.strip():
                                locator = xpath_obj.guess_xpath_button(guessable_element,"text()",element.getText())
                            else:
                                locator = xpath_obj.guess_xpath_using_contains(guessable_element,"text()",button_text.strip())
                            if len(driver.find_elements_by_xpath(locator))==1:
                                result_flag = True
                                #Check for utf-8 characters in the button_text
                                matches = re.search(r"[^\x00-\x7F]",button_text)
                                if button_text.lower() not in self.button_text_lists:
                                    self.button_text_lists.append(button_text.lower())
                                    if not matches:
                                        # Striping and replacing characters before printing the variable name
                                        print ("%s_%s = %s"%(guessable_element,button_text.strip().strip("!?.").encode('utf-8').decode('latin-1').lower().replace(" + ","_").replace(" & ","_").replace(" ","_"), locator.encode('utf-8').decode('latin-1')))
                                    else:
                                        # printing the variable name with utf-8 characters along with language counter
                                        print ("%s_%s_%s = %s"%(guessable_element,"foreign_language",self.language_counter, locator.encode('utf-8').decode('latin-1')) + "---> Foreign language found, please change the variable name appropriately")
                                        self.language_counter +=1
                                else:
                                    # if the variable name is already taken
                                    print (locator.encode('utf-8').decode('latin-1') + "----> Couldn't generate appropriate variable name for this xpath")
                                break
 
                        elif not guessable_element in self.guessable_elements:
                            print("We are not supporting this gussable element")
        
        print(self.mypaths)
        self.sendCredentials()
        return result_flag
 
    def get_variable_names(self, element):
        "generate the variable names for the xpath"
        # condition to check the length of the 'id' attribute and ignore if there are numerics in the 'id' attribute. Also ingnoring id values having "input" and "button" strings.
        if (element.has_attr('id') and len(element['id'])>2) and bool(re.search(r'\d', element['id'])) == False and ("input" not in element['id'].lower() and "button" not in element['id'].lower()):
            self.variable_name = element['id'].strip("_")
        # condition to check if the 'value' attribute exists and not having date and time values in it.
        elif element.has_attr('value') and element['value'] != '' and bool(re.search(r'([\d]{1,}([/-]|\s|[.])?)+(\D+)?([/-]|\s|[.])?[[\d]{1,}',element['value']))== False and bool(re.search(r'\d{1,2}[:]\d{1,2}\s+((am|AM|pm|PM)?)',element['value']))==False:
            # condition to check if the 'type' attribute exists
            # getting the text() value if the 'type' attribute value is in 'radio','submit','checkbox','search'
            # if the text() is not '', getting the getText() value else getting the 'value' attribute
            # for the rest of the type attributes printing the 'type'+'value' attribute values. Doing a check to see if 'value' and 'type' attributes values are matching.
            if (element.has_attr('type')) and (element['type'] in ('radio','submit','checkbox','search')):
                if element.getText() !='':
                    self.variable_name = element['type']+ "_" + element.getText().strip().strip("_.")
                else:
                    self.variable_name = element['type']+ "_" + element['value'].strip("_.")
            else:
                if element['type'].lower() == element['value'].lower():
                    self.variable_name = element['value'].strip("_.")
                else:
                    self.variable_name = element['type']+ "_" + element['value'].strip("_.")
        # condition to check if the "name" attribute exists and if the length of "name" attribute is more than 2 printing variable name
        elif element.has_attr('name') and len(element['name'])>2:
            self.variable_name = element['name'].strip("_")
        # condition to check if the "placeholder" attribute exists and is not having any numerics in it.
        elif element.has_attr('placeholder') and bool(re.search(r'\d', element['placeholder'])) == False:
            self.variable_name = element['placeholder']
        # condition to check if the "type" attribute exists and not in text','radio','button','checkbox','search'
        # and printing the variable name
        elif (element.has_attr('type')) and (element['type'] not in ('text','button','radio','checkbox','search')):
            self.variable_name = element['type']
        # condition to check if the "title" attribute exists
        elif element.has_attr('title'):
            self.variable_name = element['title']
        # condition to check if the "role" attribute exists
        elif element.has_attr('role') and element['role']!="button":
            self.variable_name = element['role']
        else:
            self.variable_name = ''
 
        return self.variable_name.lower().replace("+/- ","").replace("| ","").replace(" / ","_").  \
        replace("/","_").replace(" - ","_").replace(" ","_").replace("&","").replace("-","_").      \
        replace("[","_").replace("]","").replace(",","").replace("__","_").replace(".com","").strip("_")
 
 
 
    def guess_xpath(self, tag, attr, element):
        "Guess the xpath based on the tag,attr,element[attr]"
        #Class attribute returned as a unicodeded list, so removing 'u from the list and joining back
        if type(element[attr]) is list:
            element[attr] = [i.encode('utf-8').decode('latin-1') for i in element[attr]]
            element[attr] = ' '.join(element[attr])
        self.xpath = "//%s[@%s='%s']"%(tag,attr,element[attr])
 
        return  self.xpath
 
 
    def guess_xpath_button(self, tag, attr, element):
        "Guess the xpath for button tag"
        self.button_xpath = "//%s[%s='%s']"%(tag,attr,element)
 
        return  self.button_xpath
 
    def guess_xpath_using_contains(self, tag, attr, element):
        "Guess the xpath using contains function"
        self.button_contains_xpath = "//%s[contains(%s,'%s')]"%(tag,attr,element)
 
        return self.button_contains_xpath
    def sendCredentials(self):
        #print(globals())
        print(j.login.decoded_email); 
        print('mypaths')
        print(self.mypaths)
        a = driver.current_url #https://stackoverflow.com/questions/15985339/how-do-i-get-current-url-in-selenium-webdriver-2-python
        #def FailedLogin(BaseException):
        #    print('idk how to define error')
        driver.find_element_by_xpath(self.mypaths[0]).send_keys(j.login.decoded_email)
        driver.find_element_by_xpath(self.mypaths[1]).send_keys(j.login.decoded_password)
        driver.find_element_by_xpath(self.mypaths[3]).click()
        time.sleep(0.9)
        b = driver.current_url
        if a == b:
            loginbox = driver.find_element_by_xpath(self.mypaths[1]) #.clear()
            loginbox.clear(); loginbox.send_keys(j.login.decoded_email)
            driver.find_element_by_xpath(self.mypaths[2]).send_keys(j.login.decoded_password)
            driver.find_element_by_xpath(self.mypaths[3]).click()
        #self.mypaths = []
        #pass
#class serializer():
            #def serialize():
EncryptionDataInstance = EncryptionData()
EncryptionDataInstance.dataInitialization()
EncryptionData.activeAccounts = EncryptionDataInstance.getactiveAccounts(); print('chromeheader active accounts:'); print(EncryptionData.activeAccounts)
#gbl = globals()
print(type(EncryptionData.activeAccounts))
if type(EncryptionData.activeAccounts) == type('skills'): # lol that is hackish 
    list(EncryptionData.activeAccounts); print(type(EncryptionData.activeAccounts)); print(EncryptionData.activeAccounts)
ChromeHeader()
#driver = ChromeHeader.MyBrowserInstance
#chromeHeader = ChromeHeader()
#xpath_obj = Xpath_Util()
url = ChromeHeader.url #AttributeError: type object 'ChromeHeader' has no attribute 'url'
print(url)
driver = webdriver.Remote(command_executor=url,desired_capabilities={}) #https://duckduckgo.com/?t=ffab&q=connecting+to+an+active+webdriver+instace+python&atb=v1-1&ia=web&iax=qa
for i in EncryptionData.activeAccounts: #EncryptionData.
    #moduleToImport = 'parentDirectory.'+toImport
    print(i)
    #print(type(i, package=login))
    #gbl[i] = 
    #i = __import__('matplotlib.text') #https://stackoverflow.com/questions/8718885/import-module-from-string-variable
    j = importlib.import_module(i) #, package=j.login #https://stackoverflow.com/questions/31661188/import-files-in-python-with-a-for-loop-and-a-list-of-names
    #load_module(i)
    #exec_module(i)
    #print('j'); print(j); print(j.__dict__); print(vars(j))
    #from {}.format(i) import login # from i import login
    j.login() #each account has the same class name...lambda?
    print(j.login.decoded_email)
    xpath_obj = Xpath_Util()
    print(xpath_obj)
    print(j)
    #print(globals())
    #print(self) #ab140cda39d76ef034a1383b89c552d0
    #driver = ChromeHeader.MyBrowserInstance
    #url = ChromeHeader.url #AttributeError: type object 'ChromeHeader' has no attribute 'url'
    #print(url)
    #driver = webdriver.Remote(command_executor=url,desired_capabilities={}) #https://duckduckgo.com/?t=ffab&q=connecting+to+an+active+webdriver+instace+python&atb=v1-1&ia=web&iax=qa    
    #driver.close()   # this prevents the dummy browser
    #driver.session_id = session_id
    #driver = selenium.webdriver.remote.webdriver.WebDriver(ChromeHeader.session_id)
    #driver.session_id = ChromeHeader.session_id
    print(driver)
    #xpath_obj = Xpath_Util()
    url = j.login.url
    #driver.session_id.get(url)
    #try: #try switch tabs, wont work if only 1 tab? untested 
    p = driver.current_window_handle
    #driver.getWindowHandle() #https://stackoverflow.com/questions/43937894/can-i-tell-selenium-to-operate-in-tabs-without-switching-to-them
    #get first child window
    chwd = driver.window_handles
    print(chwd); print(p);
    for i in chwd: #https://stackoverflow.com/questions/44986194/getwindowhandles-in-selenium

    #switch focus to child window
        print(i)
        if(i==p):
            #driver.switch_to.window(i)
            driver.switch_to.window(driver.window_handles[-1]) #i + 1
        break
    time.sleep(0.9)
    print("Child window title: " + driver.title)
    #browser.refresh()
    #except:
    #    pass
    driver.get(url)
    page = driver.execute_script("return document.body.innerHTML").\
    encode('utf-8').decode('latin-1')#returns the inner HTML as a string
    soup = BeautifulSoup(page, 'html.parser')
    if xpath_obj.generate_xpath(soup) is False:
        print ("No XPaths generated for the URL:%s"%url)
    #print(vars(xpath_obj))
    #print(xpath_obj)
    #driver.find_element_by_xpath(xpath_obj.mypaths[0]).send_keys(i.login.decoded_email)
    #ChromeHeader.MyBrowserInstance.find_element_by_xpath(Xpath_Util.mypaths[1]).send_keys(j.login.decoded_password)
    #ChromeHeader.MyBrowserInstance.find_element_by_xpath(Xpath_Util.mypaths[3]).click()
    time.sleep(0.9)
    #actions = ActionChains(driver) #self.      
    #actions.key_down(Keys.CONTROL).key_down(Keys.TAB).key_up(Keys.TAB).key_up(Keys.CONTROL).perform()
    driver.execute_script("window.open('','_blank');")
    print(EncryptionDataInstance.activeAccounts)
    #EncryptionData.activeAccounts.remove(i); EncryptionDataInstance.saveArray() #https://stackoverflow.com/questions/14126726/python-throws-valueerror-list-removex-x-not-in-list
    time.sleep(0.9)
            #serialize()
#serializer()
EncryptionData.activeAccounts = []
EncryptionDataInstance.clearactiveAccounts()
driver.quit()
#https://stackoverflow.com/questions/13598035/importing-a-module-when-the-module-name-is-in-a-variable
#import importlib
#module = importlib.import_module(module_name, package=None)

#driver = ChromeHeader.MyBrowserInstance
#https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session

#exec(open('githubMain.py').read())
#driver = open('instance.py').read()	



#print(ChromeHeader.MyBrowserInstance)
#ChromeHeader.initialize()
#driver = ChromeHeader.MyBrowserInstance
#driver.get()

#ChromeHeader()

#print(ChromeHeader)
#ChromeHeader.__dict__
#vars(ChromeHeader)
#dir(ChromeHeader)
#getattr(ChromeHeader, MyBrowserInstance)
#hasattr(ChromeHeader)
#ChromeHeader.Initialize()

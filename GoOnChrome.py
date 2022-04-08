from concurrent.futures import BrokenExecutor
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import os

# getting user and password
username = input("Enter your FB username: ")
password = input("Enter your FB password: ")
Friend = input("Enter your frinds Full Name: ")
Text = input("Enter text for your frined: ")

# find version of current chrome 
def getChromeVersion():
    registryRecord = os.popen('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome" /v Version')
    registryRecordString = registryRecord.read()
    registryRecordList = registryRecordString.split(" ")
    chromeVersionFull = registryRecordList[-1]
    chromeFullVersionList = chromeVersionFull.split(".")
    chromeMajorVersion = chromeFullVersionList[0]
    return chromeMajorVersion
    
def getBrowser(chromeVersion):
    if (int(chromeVersion) > 100 or int(chromeVersion) < 95):
        print("Sorry We don't support your chrome version... You can use Chrome version: 95, 96, 97, 98, 100")
        os._exit(0)

    # get chrome drivers directory
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path.replace('\\','/')
    browser = webdriver.Chrome(dir_path + "/Drivers/Chrome V" + chromeVersion + "/chromedriver.exe")
    return browser


# Facebook Log in Function
def LogInTofacebook(browser):
    browser.get("https://www.facebook.com/")
    browser.maximize_window()

    user = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "email")))
    psswd = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "pass")))
    user.send_keys(username)
    psswd.send_keys(password)
    psswd.send_keys(Keys.ENTER)

    # Search Friend Function
def searchFriend(browser):
    search = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='search']")))
    search.click()
    search.send_keys(Friend)
    search.send_keys(Keys.ENTER)

# Message Function
def TextToFriend(browser, Text):
    # get to friends profile
    Person = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, Friend)))
    Person.click()

    # message friend
    message = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Message']")))
    message.click()
    sendbox = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Message']")))
    sendbox.click()
    sendbox.send_keys(Text)

chromeVersion = getChromeVersion()
browser = getBrowser(chromeVersion)
LogInTofacebook(browser)
searchFriend(browser)
TextToFriend(browser, Text)
from concurrent.futures import BrokenExecutor
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Ask what to do...
Answer_1 = input("Chooose Option: \n1.LogIn to FB \n2.Login to FB and find friend \n3.Login to FB, find friend and text him \n: ")

while (Answer_1 != '1' and Answer_1 != '2' and Answer_1 != "3"):
            Answer_1 = input("error: wrong input. Please put 1, 2 or 3 only: ")

#Ask how to LogIn
Answer_2 = input("How to logIn: \n1.With new FB username and password \n2.With saved username and password \n3.Delete saved username and password \n: ")
while (Answer_2 != '1' and Answer_2 != '2' and Answer_2 != "3"):
            Answer_2 = input("error: wrong input. Please put 1, 2 or 3 only: ")

# Get dir path for find passwd file and chrome driver... 
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace('\\','/')

#Check saved user and password
def chkFileContent():
    if (os.stat(dir_path +"/psswd.txt").st_size == 0):
        Answer_3 = input("\nThere are no saved username and password, do you want to add it? \nType 'Y' or 'N' \n: ")
        while (Answer_3.lower() != 'y' and Answer_3.lower() != 'n'):
            Answer_3 = input("error: wrong input. Please put 'Y' or 'N' only: ")
        if (Answer_3.lower() == "y"):
            username = input("Enter your FB username: ")
            password = input("Enter your FB password: ")
            PsswdFile = open(dir_path +"/psswd.txt", "w")
            PsswdFile.write(username + "," + password)
            PsswdFile.close()
            print("\nUser and Password succsesfully added!!!\n")
            readFileContent()
        else:
            print("\nThan LogIn with new username and password!")
            os._exit(0)

    else:
        readFileContent()

# Import saved user and password
def readFileContent():
    PsswdFile = open(dir_path +"/psswd.txt", "r")
    Content = PsswdFile.read()
    PsswdList = Content.split(",")
    PsswdFile.close()
    return GetUserAndPass(PsswdList)

# Getting user and password from the List
def GetUserAndPass(PasswdList):
    global username 
    global password
    username = PasswdList[0]
    password = PasswdList[1]
    return username, password

# Delete saved user and password
def delFileContent():
    DelAnswer = input("\nDo you really want to delete saved username and password? \nType 'Y' or 'N':")
    while (DelAnswer.lower() != 'y' and DelAnswer.lower() != 'n'):
            DelAnswer = input("error: wrong input. Please put 'Y' or 'N' only: ")
    if (DelAnswer.lower() == "y"):
        open(dir_path +"/psswd.txt", 'w').close()
        print("\nUsername and password deleted successfully!!!\n")
    else:
        print("\nOkay, Than continue!!!\n")

    Answer_2 = input("How to logIn: \n1.With new FB username and password \n2.With saved username and password \n3.Delete saved username and password \n: ")
    while (Answer_2 != '1' and Answer_2 != '2' and Answer_2 != "3"):
        Answer_2 = input("error: wrong input. Please put 1, 2 or 3 only: ")

    if (Answer_2 == "1"):
        ForNewPass()
    elif (Answer_2 == "2"):
        chkFileContent()
    elif (Answer_2 == "3"):
        delFileContent()
    


# Logging with new FB user and password
def ForNewPass():
    global username
    global password
    username = input("Enter your FB username: ")
    password = input("Enter your FB password: ")
    Answer_4 = input("Do you want to save username and password? Type 'Y' or 'N': ")

    while (Answer_4.lower() != 'y' and Answer_4.lower() != 'n'):
            Answer_4 = input("error: wrong input. Please put 'Y' or 'N' only: ")

    if (Answer_4.lower() == "y"):

        # Check If there are already saved user and password
        if (os.stat(dir_path +"/psswd.txt").st_size != 0):
            Answer_5 = input("\nYou already have saved user and password, overwrite it? \nType 'Y' or 'N': ")

            while (Answer_5.lower() != 'y' and Answer_5.lower() != 'n'):
                Answer_5 = input("error: wrong input. Please put 'Y' or 'N' only: ")

            if (Answer_5.lower() == "y"):
                PsswdFile = open(dir_path +"/psswd.txt", "w")
                PsswdFile.write(username + "," + password)
                PsswdFile.close()
                print("\nUser and Password succsesfully added!!!\n")

            elif (Answer_5.lower() == "n"):
                print("\nOkay, than continue\n")
        
        # If there are no saved user and password yet     
        else:
            PsswdFile = open(dir_path +"/psswd.txt", "w")
            PsswdFile.write(username + "," + password)
            PsswdFile.close()
            print("\nUser and Password succsesfully added!!!\n")
        
    if (Answer_4.lower() == "n"):
        print("\nLogging In!!!\n")

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
        print("\nSorry We don't support your chrome version... You can use Chrome version: 95, 96, 97, 98, 99 or 100")
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

# When Logging In
if (Answer_1 == "1"):
    if (Answer_2 == "1"):
        ForNewPass()
    elif (Answer_2 == "2"):
        chkFileContent()
    elif (Answer_2 == "3"):
        delFileContent()
    chromeVersion = getChromeVersion()
    browser = getBrowser(chromeVersion)
    LogInTofacebook(browser)

# When Logging in and finding frind
elif (Answer_1 == "2"):
    if (Answer_2 == "1"):
        ForNewPass()
    elif (Answer_2 == "2"):
        chkFileContent()
    elif (Answer_2 == "3"):
        delFileContent()
    Friend = input("Enter your frinds Full Name: ")
    chromeVersion = getChromeVersion()
    browser = getBrowser(chromeVersion)
    LogInTofacebook(browser)
    searchFriend(browser)

# When logging in finding friend and texting him
elif (Answer_1 == "3"):
    if (Answer_2 == "1"):
        ForNewPass()
    elif (Answer_2 == "2"):
        chkFileContent()
    elif (Answer_2 == "3"):
        delFileContent()
    Friend = input("Enter your frinds Full Name: ")
    Text = input("Enter text for your frined: ")
    chromeVersion = getChromeVersion()
    browser = getBrowser(chromeVersion)
    LogInTofacebook(browser)
    searchFriend(browser)
    TextToFriend(browser, Text)

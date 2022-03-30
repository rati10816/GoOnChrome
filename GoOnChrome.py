from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 
import os

# getting user and password
username = input("Enter your FB username: ")
password = input("Enter your FB password: ")
# Friend = input("Enter your frinds name: ")
# Text = input("Enter text for your frined: ")

# find version of current chrome 
version = os.popen('reg query "HKLM\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome"')
output = version.read()

# get chrome drivers directory
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace('\\','/')

# Facebook Log in Function
def facebook():
    browser.get("https://www.facebook.com/")
    browser.maximize_window()

    user = browser.find_element_by_id('email')
    psswd = browser.find_element_by_id('pass')

    time.sleep(0.5)
    user.send_keys(username)
    time.sleep(0.5)
    psswd.send_keys(password)
    time.sleep(0.5)
    psswd.send_keys(Keys.ENTER)

    # Search Friend
    # time.sleep(15)
    # search = browser.find_element_by_class_name("oajrlxb2 f1sip0of hidtqoto e70eycc3 hzawbc8m ijkhr0an pvl4gcvk sgqwj88q b1f16np4 hdh3q7d8 dwo3fsh8 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz br7hx15l h2jyy9rg n3ddgdk9 owxd89k7 rq0escxv oo9gr5id mg4g778l buofh1pr g5gj957u ihxqhq3m jq4qci2q hpfvmrgz lzcic4wl l9j0dhe7 iu8raji3 l60d2q6s dflh9lhu hwnh5xvq scb9dxdr qypqp5cg rmlgq0sb dzqu5etb aj8hi1zk kd8v7px7 r4fl40cc m07ooulj mzan44vs")
    # search.send_keys(Friend)
    # search.send_keys(Keys.ENTER)

# find chrome driver for this version and login to facebook
if(output.find("100") != -1):
    browser = webdriver.Chrome(dir_path+"/Drivers/Chrome V100/chromedriver.exe")
    facebook()

elif(output.find("99") != -1):
    browser = webdriver.Chrome(dir_path+"/Drivers/Chrome V99/chromedriver.exe")
    facebook()

elif(output.find("98") != -1):
    browser = webdriver.Chrome(dir_path+"/Drivers/Chrome V98/chromedriver.exe")
    facebook()

elif(output.find("97") != -1):
    browser = webdriver.Chrome(dir_path+"/Drivers/Chrome V97/chromedriver.exe")
    facebook()

elif(output.find("96") != -1):
    browser = webdriver.Chrome(dir_path+"/Drivers/Chrome V96/chromedriver.exe")
    facebook()

elif(output.find("95") != -1):
    browser = webdriver.Chrome(dir_path+"/Drivers/Chrome V95/chromedriver.exe")
    facebook()

else:
    print("Sorry We don't support your chrome version... You can use Chrome version: 95, 96, 97, 98, 100")
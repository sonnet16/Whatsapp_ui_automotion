import sys,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


chrome_browser = webdriver.Chrome(executable_path=r'D:\New folder\Selinium CromeDriver\chromedriver.exe')
chrome_browser.get('https://web.whatsapp.com/')
time.sleep(15)
print('SuccessFully  Login')
# Scan QR Code And Enter
try:
    #Search Contact
    contact = "oli"
    msg = "This msg sent By chatbot"
    search_box = chrome_browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    time.sleep(15)
    #Select Message Box And Sent message
    msg_box = chrome_browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
    msg_box.send_keys(msg)
    msg_box.send_keys(Keys.ENTER)
    print('Message Sent Successfully')
    time.sleep(15)
    #Menu Bar Open
    menu_bar = chrome_browser.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/div')
    menu_bar.send_keys(Keys.ENTER)
    time.sleep(10)
    # Logout Option Click
    logout = chrome_browser.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[6]/div[1]')
    logout.send_keys(Keys.ENTER)
    time.sleep(5)
    print('Logout Successfully')
    time.sleep(10)
    chrome_browser.close()
    sys.exit()

except NoSuchElementException as Se:
    print("UserName or Number  Not Found")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# s = Service('C:\Program Files (x86)\chromedriver.exe')
# browser = webdriver.Chrome(service=s)
# url = 'https://www.google.com'
# browser.get(url)

PATH = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://techwithtim.net")


# fname = input()
# lname = input()
#
# print(fname, lname)

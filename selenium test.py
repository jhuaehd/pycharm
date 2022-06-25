from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time

PATH = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)
driver.get("https://techwithtim.net")
print("This page is : ", driver.title)

search = driver.find_elements_by_name()
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()



# fname = input()
# lname = input()
#
# print(fname, lname)

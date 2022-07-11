

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

import time

# gets the chromedriver path
PATH = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

# directly go to the provided url
driver.get("https://www.dropbox.com/login")
# driver.find_element_by_name("q").send_keys("javatpoint")
# driver.find_element_by_name("q").send_keys(Keys.ENTER)

# gets the element name in the page and send following string to particular element name
# driver.find_element("name", "s").send_keys("python")
driver.find_element(By.NAME, value="login_email").send_keys("joshuaehd.silvio.37@gmail.com")
driver.find_element(By.NAME, value="login_password").send_keys("123456")
# driver.find_element(By.CSS_SELECTOR, value="type:submit").click()
driver.find_element(By.XPATH, value="//button[@type='submit']").click()
# click_button = driver.find_element(By.CLASS_NAME, "login-button")
# print(click_button.get_attribute('type'))



# send enter key to the element
# since the search box name="s" has no enter button, let's send enter key to the search box
# driver.find_element("name", "s").send_keys(Keys.ENTER)
# time.sleep(5)
# driver.close()



print("Test Completed Successfully ")
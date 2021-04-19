from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

userName = driver.find_element_by_name("userName")
print(userName.is_enabled())
print(userName.is_displayed())
# print(userName.is_selected())  # Redio Buttion

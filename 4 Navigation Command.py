from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
print(driver.title)

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

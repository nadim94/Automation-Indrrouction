from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")
link = driver.find_elements(By.TAG_NAME, "a")

print(len(link))

for links in link:
    print(links.text)

driver.find_element(By.LINK_TEXT, "REGISTER")
driver.find_element(By.PARTIAL_LINK_TEXT, "REG")

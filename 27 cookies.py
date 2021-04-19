from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")
cook = driver.get_cookies()
print(cook)
print(len(cook))

# Add Cookie
cookie = {'name': 'mycookie', 'value': '123456'}
driver.add_cookie(cookie)
cook = driver.get_cookies()
print(cook)
print(len(cook))

# Delete Cookie
driver.delete_cookie('mycookie')
cook = driver.get_cookies()
print(cook)
print(len(cook))
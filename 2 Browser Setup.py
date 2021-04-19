from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver2 = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.28.0-win64\geckodriver.exe")
driver2.get("https://www.google.com/")
print(driver2.title)
driver2.close()

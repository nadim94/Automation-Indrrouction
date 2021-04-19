from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")
driver.maximize_window()
time.sleep(4)

driver.save_screenshot("C:/Users/Md. Nadim Kaysar/Desktop/homepage.png")
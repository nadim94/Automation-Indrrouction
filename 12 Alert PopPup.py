from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[2]/div/aside/div/div[2]/div[1]/button").click()
time.sleep(5)

# driver.switch_to_alert().accept()
# driver.switch_to.alert.accept()  # Alert Window using Ok Button
driver.switch_to.alert.dismiss()  # Alert Window using Ok Cancel

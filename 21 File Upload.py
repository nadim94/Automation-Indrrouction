from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("C://Users/Md. Nadim Kaysar/Desktop/test_loss.PNG")

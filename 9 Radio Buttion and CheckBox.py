from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
# print(status)
time.sleep(5)
# driver.find_element_by_id("RESULT_RadioButton-7_0").click()

driver.find_element_by_id("RESULT_CheckBox-8_0").click()
driver.find_element_by_id("RESULT_CheckBox-8_1").click()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

time.sleep(5)
input_boxes = driver.find_elements(By.CLASS_NAME, 'text_field')
a = len(input_boxes)
print(a)

driver.find_element_by_id("RESULT_TextField-1").send_keys("NadimKaysar")

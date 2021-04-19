from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("Demo Site for table data read")
driver.find_elements_by_xpath("/html/body/table/tbody/tr")

row = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))  # Count Number of row

cols = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))  # Count Number of Columns
print(row)
print(cols)

for r in range(2, row+1):
    for c in range(1, cols+1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value)
    print()


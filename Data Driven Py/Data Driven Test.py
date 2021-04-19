import xlutils
import xlutils3
import XLread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
time.sleep(5)

path = "C:/Users/Md. Nadim Kaysar/Desktop/testdata.xlsx"

row = XLread.getRowcount(path, 'Sheet1')
for r in range(2, row+1):
    username = XLread.readData(path, "Sheet1", r, 1)
    pass_word = XLread.readData(path, "Sheet1", r, 2)
    print(username)
    print(pass_word)
    driver.find_element_by_xpath("userName").send_keys(username)
    driver.find_element_by_name("password").send_keys(pass_word)

    driver.find_element_by_name("submit").click()

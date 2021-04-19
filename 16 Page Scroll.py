from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
# driver.execute_script("window.scrollBy(0,1000)", "")  # Scroll By Pixel wise

# Scroll Down By Element
# flag = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# Scroll Down Till End The Page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

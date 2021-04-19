from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Note:  Full Complete hoy nai
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.expedia.com/")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/ul/li[2]/a").click()

time.sleep(5)
driver.find_element_by_xpath("//*[@id='location-field-leg1-origin']").send_keys("San Francisco (SFO - San Francisco Intl.)")
driver.find_element_by_xpath("//*[@id='location-field-leg1-destination']").send_keys("NYC")

driver.find_element_by_id("d1-btn").clear()
driver.find_element_by_id("d1-btn").send_keys("01/01/2020")

driver.find_element_by_id("d2-btn").clear()
driver.find_element_by_id("d2-btn").send_keys("10/01/2020")

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div[3]/div/figure/div[3]/div/div/div/div[2]/div/form/div[3]/div[2]/button").click()

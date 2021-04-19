from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
right_click = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions = ActionChains(driver)

actions.context_click(right_click).perform()   # Mouse Right Click Action

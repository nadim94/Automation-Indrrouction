from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
time.sleep(5)
# Mouse Hover Action
admin = driver.find_element_by_id("menu_admin_viewAdminModule")
user_management = driver.find_element_by_id("menu_admin_UserManagement")
user = driver.find_element_by_id("menu_admin_viewSystemUsers")
action = ActionChains(driver)

action.move_to_element(admin).move_to_element(user_management).move_to_element(user).click().perform()
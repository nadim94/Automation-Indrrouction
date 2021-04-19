from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import logging

# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

# driver.get("https://www.amazon.in/")
# driver.maximize_window()

logging.basicConfig(filename="C:/Users/Md. Nadim Kaysar/Desktop/homepage.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%Y/%m/%d %I:%M:%S %p',
                    level=logging.DEBUG)

logging.debug("This is debug document")
logging.info("This is info")
logging.warning("This is warning")
logging.error("This is error")
logging.critical("This is critical")

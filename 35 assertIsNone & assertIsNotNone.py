import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class MyTestCase(unittest.TestCase):
    def test_google(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        # Variable value should be None
        # self.assertIsNone(driver)

        # variable value should be Not None
        self.assertIsNotNone(driver)


if __name__ == '__main__':
    unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class MyTestCase(unittest.TestCase):
    def test_google(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        pageTitle = self.driver.title

        self.assertEqual("Googleddd", pageTitle, "Page Name Title is Not Same")


if __name__ == '__main__':
    unittest.main()

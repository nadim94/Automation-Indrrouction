import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class MyTestCase(unittest.TestCase):
    def test_google(self):
        list = {"python", "Java", "selenium"}

        # self.assertIn("pythonaaa", list)
        self.assertNotIn("ruby", list)


if __name__ == '__main__':
    unittest.main()

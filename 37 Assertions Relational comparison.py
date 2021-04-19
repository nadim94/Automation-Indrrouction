import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class MyTestCase(unittest.TestCase):
    def test_google(self):
        # self.assertGreater(100, 100)
        # self.assertGreaterEqual(100, 1007)
        self.assertLess(10, 100)
        self.assertLessEqual(100, 100)


if __name__ == '__main__':
    unittest.main()

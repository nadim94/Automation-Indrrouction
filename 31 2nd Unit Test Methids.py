import unittest


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("login check")

    @classmethod
    def tearDown(cls) -> None:
        print("logout check")

    @classmethod
    def setUpClass(cls) -> None:
        print("Start Application")

    @classmethod
    def tearDownClass(cls) -> None:
        print("Close Application")

    def test_search(self):
        print("This is search method")

    def test_advanchedSearch(self):
        print("Advanced Search method")

    def test_prepaid_method(self):
        print("Print prepaid method")

    def test_postpaid_method(self):
        print("Print Post Paid method")


if __name__ == '__main__':
    unittest.main()

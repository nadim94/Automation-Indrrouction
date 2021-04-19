import unittest


class FirstTestClass(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("Test Basic Search")


    @unittest.skip("I am Skippig this test because it is not ready")
    def test_advanched_serach(self):
        print("Test Advached Search")

    @unittest.skipIf(1 == 1, "Skippig this test because it is not ready")
    def test_pre_paid_recharge(self):
        print("Pre Paid Recharge")

    def test_post_paid_recharge(self):
        print("Post Paid Recharge")

    def test_login_by_gmail(self):
        print("Gmail Login")


if __name__ =="__main__":
    unittest.main()
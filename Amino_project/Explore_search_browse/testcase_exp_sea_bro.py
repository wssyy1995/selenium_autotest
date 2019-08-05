import unittest
import time
from selenium import webdriver
from HTMLTestRunner import HTMLTestRunner
from explore_search_browse_model import explore,search



class Test_ex_se_bro(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://aminoapps.com")
        print('start test')

    def testex(self):
        explore(self.driver)


    def testsea(self,):
        search(self.driver)


    def testbro(self):

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print('end test')


unittest.main()

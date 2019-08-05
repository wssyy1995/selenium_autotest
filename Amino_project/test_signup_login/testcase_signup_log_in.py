import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from signup_login_model import login_telephone,logout,login_email,logtestprint
import pymysql

mscon = pymysql.connect(host='localhost', user='root', password='wssyy,yyqx1128', database='yayandb1')
cursor = mscon.cursor()
aasql = "select username,password from amino_tele"
cursor.execute(aasql)
ret = cursor.fetchall()

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://aminoapps.com")
        print('start test')



    def test_login_telephone_with_right(self):
        self.username=ret[0][0]
        self.password=ret[0][1]
        login_telephone(self.driver,self.username,self.password)
        try:
            self.driver.find_element_by_xpath("/html/body/header/div/div/nav/ul/li[3]/a/img")
        except NoSuchElementException:
            find=False
        else:
            find=True
            print('login successsfully')
        self.assertTrue(find)




    # def test_login_telephone_with_wrong(self):
    #     login_telephone(self.driver,ret)
    #     try:
    #         self.driver.find_element_by_xpath("/html/body/header/div/div/nav/ul/li[3]/a/img")
    #     except NoSuchElementException:
    #         find = False
    #     else:
    #         find = True
    #         print('login successsfully')
    #
    #         self.assertTrue(find)


    def test_logout(self):
        # self.username = ret[0][0]
        # self.password = ret[0][1]
        # login_telephone(self.driver, self.username, self.password)
        logout(self.driver)
        try:
            self.driver.find_element_by_xpath("/html/body/header/div/div/nav/ul/li[3]/a/img")
        except NoSuchElementException:
            find=False
        else:
            find=True
        self.assertFalse(find)
        print('logout seccessfully')



    def tearDown(self) -> None:
        print('test end')


# if __name__ == '__main__':
#     suite=unittest.TestSuite()
#     suite.addTest(Login("test_logout"))
#
#     runner=unittest.TextTestRunner()
#     runner.run(suite)





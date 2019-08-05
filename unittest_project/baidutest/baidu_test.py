from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("http://www.baidu.com")


    def test_baidu_search(self):
        '''
        keys:test1

        '''
        self.driver.find_element_by_id('kw').send_keys('test1')
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        print(self.driver.title)
        self.assertEqual(self.driver.title,'test1_百度搜索')


    def test_baidu_search2(self):
        self.driver.find_element_by_id('kw').send_keys('test2')
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        print(self.driver.title)
        self.assertEqual(self.driver.title, 'test2_百度搜索')



    def tearDown(self):
        self.driver.quit()



# #定义
# suite=unittest.TestSuite()
# suite.addTest(Baidu('test_baidu_search'))
# suite.addTest(Baidu('test_baidu_search2'))

# #定义报告存放路径
# report=open('./'+time.ctime()+'.html','wb')
# #定义测试报告
# runner=HTMLTestRunner(stream=report,title='baidusearch_report',description='the report of baidu search')
# runner.run(suite)
# report.close()
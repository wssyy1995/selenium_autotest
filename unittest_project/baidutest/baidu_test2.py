from selenium import webdriver
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

class Baidu2(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("http://www.baidu.com")


    def test_baidu_click(self):
        self.driver.find_element_by_link_text('新闻').click()
        time.sleep(2)
        print(self.driver.title)
        self.assertEqual(self.driver.title,'百度新闻——海量中文资讯平台')


    def test_baidu_click2(self):
        self.driver.find_element_by_link_text('地图').click()
        time.sleep(2)
        print(self.driver.title)
        self.assertEqual(self.driver.title, '百度地图')



    def tearDown(self):
        self.driver.quit()



# #定义测试集
# suite=unittest.TestSuite()
# suite.addTest(Baidu2('test_baidu_click'))
# suite.addTest(Baidu2('test_baidu_click2'))
#
#
# #定义报告存放路径
# report=open('./'+time.ctime()+'.html','wb')
# #定义测试报告
# runner=HTMLTestRunner(stream=report,title='baidusearch_report',description='the report of baidu search')
# runner.run(suite)
# report.close()
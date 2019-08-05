#方式一：运行所有包含在该模块中以'test'命名开头的测试方法


# if __name__ =='__main__':
#     #运行所有包含在该模块中以'test'命名开头的测试方法
#     #unittest.main()
#方式二： 当不想执行所有测试用例时，构造测试集
#
#     suite=unittest.TestSuite()
#     suite.addTest(PrimeTest('test_prime'))
#     #执行测试
#     runner=unittest.TextTestRunner()
#     runner.run(suite)

#方式三：在一个专门的runtest.py文件中，通过discover，将需要运行的测试文档以一种特定的命名格式，来添加


import unittest
import time
from HTMLTestRunner import HTMLTestRunner


test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

#定义测试报告
report=open('./report_signup_login/'+time.ctime()+'.html','wb')
runner=HTMLTestRunner(stream=report,title='signup_login_report',description='the report of aminoapps signup')

runner.run(discover)

report.close()



#方式三：在一个专门的runtest.py文件中，通过discover，将需要运行的测试文档以一种特定的命名格式，来添加


import unittest


1.
test_dir='./'
discover=unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')
# start_dir：要测试的模块名/测试用例所在的目录
# pattern:表示测试用例文件名的匹配规则
# discover()方法自动根据测试目录test_dir，递归找到子目录下符合'test*.py'命名规则的文件，将查找到的测试用例组装到测试套件中；再用run（）方法执行测试
# 创建runner对象
runner=unittest.TextTestRunner()
runner.run(discover)





2.自动生成HTML测试报告
# （1）下载HTMLTestRunner.py文件：地址http://tungwaiyip.info/software/HTMLTestRunner.html
# (2)、将该文件保存在python安装路径下的lib/site-package文件夹中。在文件中能import HTMLTestRunner成功，即配置成功。

import time
from HTMLTestRunner import HTMLTestRunner

# 定义报告存放路径
# report_address=open('./html_report/'+time.ctime()+'.html','wb')
# 创建HTMLTestRunner类的runner对象
 runner=HTMLTestRunner(stream=report_address,title='signup_login_report',description='the report of yayan autotest')
#
# runner.run(discover)
#
# report.close()

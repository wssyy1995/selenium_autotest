# 一.自动化测试模型介绍：
# (1)线性测试：录制或编写对应用程序的操作步骤，单纯地模拟用户完整的操作场景，每一个脚本都是完整且独立的
# (2)模块化驱动测试：将重复的操作独立成公共模块
# (3)数据驱动操作：模块数据的参数化，输入数据不同从而引起输出结果吧托尼盖
# (4)关键字驱动测试：数据驱动，把"数据"换成"关键字"
#
# 二.模块化驱动测试用例
# 例子：将登陆&退出百度的功能封装到函数中
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(5)  #非常重要，在定义好driver对象后必须设置隐式等待
# driver.get("http://www.baidu.com")

#登录方法
# def bdlogin():
#     driver.find_element_by_link_text("登录").click()
#     time.sleep(1)
#     driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
#     driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("18221091524")
#     driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("123456ff")
#     driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
#
# def bdlogout():
#     print('log out')
#     usename=driver.find_element_by_xpath("//*[@id='s_username_top']/span")
#     ActionChains(driver).move_to_element(usename).perform()
#     driver.find_element_by_xpath('// *[ @ id = "s_user_name_menu"] / div / a[4]').click()
#     driver.find_element_by_xpath("//*[@id='tip_con_wrap']/div[3]/a[3]").click()

#创建一个单独的模块,导入模块
# import sys
# sys.path.append("/Users/suyayan/PycharmProjects/selenium_autotest/common_function")
# import time
# from bdaction import Log1
#
# Log1.login1(driver)



# 二.数据驱动测试用例(使用模块的完整版)

(1)# 修改模块，使得driver成为了类的对象,账号和密码是可以传入的参数
#先将内置模块导入
from selenium import webdriver
# import sys
# sys.path.append("/Users/suyayan/PycharmProjects/selenium_autotest/common_function")
# #导入登录的模块
# from bdaction import Logintest
# bd=Logintest()
# bd.login("18221091524","123456ff")


#(2)读取文件的中的数据
from selenium import webdriver
import sys
sys.path.append("/Users/suyayan/PycharmProjects/selenium_autotest/common_function")
from bdaction import Logintest

readtest = open('/Users/suyayan/Downloads/pyfileoperation/readtest.txt',mode='r')
content = readtest.readlines()
for i in content:
    print(i)
    list=i.split(",")
    print('list:',list)
    username=list[0].strip(r"\n")
    print(username)
    pwd = list[1].strip(r"\n")
    print(pwd)
    bd = Logintest()
    bd.login(username,pwd)
    print('------------------')





















#
# bdlogin()
# time.sleep(5)
# bdlogout()































# time.sleep(20)
# driver.quit()


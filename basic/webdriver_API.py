from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
driver=webdriver.Chrome()
driver.implicitly_wait(2)
#driver.get("https://passport.csdn.net/login")
#driver.get("https://www.baidu.com/")
#打开本地html:
    # localfile='file:///'+os.path.abspath('html_test.html')
    # print(file)
    # driver.get(localfile)


# 一.定位元素
# 百度输入框:<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
#
# 通过id定位
# driver.find_element_by_id("kw").send_keys("find_element_by_id")
# 动态id:auto-id
# driver.find_element_by_xpath('//*[contains(@id,"auto-id")]')
#
# 通过name定位
# driver.find_element_by_name("wd").send_keys('find_element_by_name')
#
# 通过class_name定位
# driver.find_element_by_class_name("s_ipt").send_keys("find_element_by_class_name")
#
# 百度文本链接:<a href="http://news.baidu.com" target="_blank" class="mnav">新闻</a>
#
# 通过link文本定位
# driver.find_element_by_link_text("新闻").click()
#
# 通过linkd的部分文本定位
# driver.find_element_by_partial_link_text("新").click()


# 通过Xpath定位百度输入框
# 绝对路径定位
# driver.find_elements_by_xpath("/html/body/div/div[2]/div/div/div/form/span/input")
# 元素属性定位
# driver.find_elements_by_xpath("//*[@id='kw']")
# 使用逻辑运算符
# driver.find_elements_by_xpath("//input[@id='kw' and @class='su']")
#
# 通过css定位
# class属性定位：点号（.）表示通过class属性来定位元素
# driver.find_elements_by_css_selector(".s_ipt")
# id属性定位：井号(#)便是通过id属性定位元素
# driver.find_elements_by_css_selector("#kw")
# 标签名定位：标签名重复率大，很难找到想要的元素
# driver.find_elements_by_css_selector(input)
# 通过属性定位
# driver.find_elements_by_css_selector("[name='kw']/[type='submit']")
# 组合定位:寻找一个有bg s_ipt_wr的class属性的span标签>往下一级找有class属性叫s_ipt的input标签
# driver.find_elements_by_css_selector("span.bg s_ipt_wr>input.s_ipt")


#二.控制浏览器

#控制浏览器窗口的大小
# driver.set_window_size(200,300)
# driver.maximize_window()

#控制浏览器后退，前进
# driver.get("http://dict.youdao.com/")
# time.sleep(2)
# driver.get("https://www.icourse163.org/")
# time.sleep(2)
# driver.back() #回到上一个网页
# time.sleep(2)
# driver.forward() #前进到上一个网页

#模拟浏览器刷新
#driver.refresh()

#三.简单元素操作
#clear():清除文本
#send_keys(*value)
#click():单击元素
#submit():提交表单

#例子：b站登录
# driver.find_element_by_id("login-username").clear()
# driver.find_element_by_id("login-username").send_keys("18221091524")
# driver.find_element_by_id("login-passwd").send_keys("123456ff")
# driver.find_element_by_link_text("登录").click()
# driver.find_element_by_css_selector("#geetest-wrap > ul > li.btn-box > a.btn.btn-login").click()
# driver.find_element_by_xpath("//*[@id='geetest-wrap']/ul/li[5]/a[1]").click()

#例子：youdao 翻译
# driver.find_element_by_id("translateContent").send_keys("hello")
# driver.find_element_by_id("translateContent").submit() #submit()模拟了在输入文本之后"回车"的操作


#四.鼠标事件

#导入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains


#context_click(): 右击
#定位到要右击的元素
#right_click=driver.find_element_by_link_text("查看单词本")
#对定位到的元素执行鼠标右键操作, perform()执行所有ActionChains中存储的行为
#ActionChains(driver).context_click(right_click).perform()

#move_to_element(): 鼠标悬停
# move_to_element=driver.find_element_by_link_text("查看单词本")
# ActionChains(driver).move_to_element(move_to_element).perform()

# double_click():  双击
# d_click=driver.find_element_by_link_text("查看单词本")
# ActionChains(driver).double_click(d_click).perform()

# drag_and_drop(source,target): 在源元素上按住鼠标左键，然后移动到目标元素上释放
# source=driver.find_element_by_link_text("查看单词本")
# # target=driver.find_element_by_id("translateContent")
# # ActionChains(driver).drag_and_drop(source,target).perform()


#五.键盘事件:可以模拟键盘上的按键
#导入keys模块
from selenium.webdriver.common.keys import Keys

#模拟键盘输入内容
# driver.find_element_by_id("kw").send_keys('sendkeys')
# time.sleep(2)
#模拟键盘删除最后的一个字符
#driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#模拟键盘输入空格键
# time.sleep(2)
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)

#模拟键盘ctrl+a,c,v
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'c')
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

#模拟键盘回车键来代替单击操作
# driver.find_element_by_id("su").send_keys(Keys.ENTER)


#六.获得验证信息


# print('打印登录前页面信息')
# current_title=driver.title
# print(current_title)
# current_url=driver.current_url
# print(current_url)
# print('---------------')
#
#
# #执行登录
# driver.find_element_by_id("switchAccountLogin").click()
# driver.switch_to_frame(0) #当要定位的元素在一个Frame里，需要切换到这个frame
# driver.find_element_by_name("email").send_keys("18221091524")
# driver.find_element_by_name("password").send_keys("123456ff")
# driver.find_element_by_id("dologin").click()
# driver.switch_to.default_content()
#
# print('打印登录后页面信息')
# current_title=driver.title
# print(current_title)
# current_url=driver.current_url
# print(current_url)



#七.元素等待


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#显示等待
#WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
#baiduinput=WebDriverWait(driver,5,0.5).until(EC.presence_of_all_elements_located((By.ID,"kw")))
#baiduinput[0].send_keys('selenium') #当我没有加[0]的时候，报错'list' object has no attribute 'send_keys'



#隐式等待: #在创建deriver对象之后就设置一个等待时间，只要找不到某个元素就报错
# from selenium.common.exceptions import NoSuchElementException
# driver.implicitly_wait(5)
# driver.get("https://www.baidu.com/")
# try:
#     print(time.ctime())
#     driver.find_element_by_id("kw1").send_keys("百度隐式等待1")
# except NoSuchElementException:
#     print("没有这个元素")
# finally:
#     print(time.ctime())
#
# driver.find_element_by_id("kw").send_keys("百度隐式等待2")


#八.定位一组元素:在element后面加s
#find_elements_by...
# driver.get("http://www.w3school.com.cn/tiy/t.asp?f=html_checkboxes")
# driver.switch_to.frame("iframeResult")  #找不到元素的时候一定要看看在不在iframe里
# checkboxs=driver.find_elements_by_css_selector('[type="checkbox"]')
# checkboxs=driver.find_elements_by_xpath("//input[@type='checkbox']")
# print(checkboxs)
# for i in checkboxs:
#     i.click()
#     time.sleep(1)
#     print('click')
#
# driver.switch_to.default_content() #当要再找frame之外的元素，必须切回主文档
# dark=driver.find_element_by_link_text("暗黑模式")
# print(dark)
# dark.click()

# 九.多表单切换:对于frame/iframe表单内嵌页面上的元素无法直接定位，需要通过switch_to frame()将当前定位的主体切换为frame/iframe表单的内嵌页面中
# switch_to.frame("frame的id，或者名字，或者索引")
# switch_to.parent_content() 跳出当前一层表单
# switch_to.default_content() 跳回最外层的页面


#十.多窗口切换（重要）:当在窗口1打开一个新的页面，窗口句柄不会自动切换到当前窗口，需要用脚本切换，否则无法定位新窗口的元素
# driver.get("https://www.baidu.com/")
# #获得百度搜索窗口句柄
# search_window=driver.current_window_handle
# print('search_window:',search_window)
# time.sleep(3)
# driver.find_element_by_link_text("登录").click()
# time.sleep(1)
#
# #进入注册窗口
# driver.find_element_by_xpath("//*[@id='passport-login-pop-dialog']/div/div/div/div[4]/a").click()
# time.sleep(3)
#
#
# #获得当前所有打开窗口的句柄
# all_handles=driver.window_handles
# print(all_handles)
# time.sleep(1)
#
#
# for handle in all_handles:
#     if handle!=search_window:
#         driver.switch_to.window(handle)
#         register_window=driver.current_window_handle
#         print('change to register window')
#         driver.find_element_by_link_text("《百度用户协议》").click() #只有将窗口句柄切换到窗口2，才能对窗口2的元素进行操作
# print('register_window:',register_window)
# time.sleep(3)
# print('start ')
# for i in range(10):
#     driver.switch_to.window(search_window)
#     time.sleep(3)
#     driver.switch_to.window(register_window)
#     time.sleep(3)


#十一.警告框处理：switch_to_alert()定位到alert/confirm/prompt，然后使用text/accept,dismiss/send.keys等方法进行操作

# driver.get("https://www.baidu.com/")
# driver.find_element_by_css_selector("#form > span.bg.s_ipt_wr.quickdelete-wrap > span.ipt_rec").click()
# driver.switch_to_alert().dismiss()/accept()/text

#十二.上传文件

# localfile='file://'+os.path.abspath('html_test.html')
# driver.get(localfile)
# print(localfile)
# #定位<input type='file' name='file'>这个元素，直接给这个元素send_keys文件
# driver.find_element_by_name('file').send_keys('/Users/suyayan/Downloads/pyfileoperation/signuptest.text')

#十三.下载文件
#AutoIt




# 十四：操作cookie
# get_cookies:获得所有cookie信息
# get_cokie(name)：返回字典的key为"name"的cookie信息
# add_cookie(cookie_dic):添加cookie
# delete_cookie(name,optionsString):删除cookie信息
# delete_all_cookies:删除所有cookie信息

# driver.get("https://www.baidu.com/")
# #driver.find_element_by_id("kw").send_keys("find_element_by_id")
#
#
# cookie1=driver.get_cookies()
# for i in cookie1:
#     print(i)
#
#
#
# time.sleep(25)
# print('after log in \n  ')
#
# cookie2=driver.get_cookies()
# for i in cookie2:
#     print(i)
#
# driver.delete_all_cookies()
# time.sleep(2)
# driver.refresh()
# print('after delete cookies \n \n  ')
#
# cookie3=driver.get_cookies()
# for i in cookie3:
#     print(i)



#十五.调用javascript

# driver.get("https://www.baidu.com/")
# driver.find_element_by_id("kw").send_keys("调用javascript")
# driver.find_element_by_id("su").click()
# time.sleep(1)
# driver.set_window_size(600,600)
# time.sleep(1)
# js="window.scrollTo(200,200)"  #window.scrollTo(左边距，上边距)
#将页面的滚动条滑动到页面的最下方
#js="window.scrollTo(100, document.body.scrollHeight)"
# time.sleep(1)
# driver.execute_script(js)

#十六：处理html5的视频播放


# driver.get("https://www.bilibili.com/video/av58999361")
# video=driver.find_element_by_xpath('//*[@id="bilibiliPlayer"]/div[1]/div[1]/div[8]/video')
# print('find the video')
# #返回播放文件的地址
# url=driver.execute_script("return arguments[0].currentSrc",video)
# print(url)
# time.sleep(2)
# #播放视频
# print('start')
# driver.execute_script("return arguments[0].play()",video)
# time.sleep(15)
# #暂停视频
# print('stop')
# driver.execute_script("return arguments[0].pause()",video)



#十七.窗口截图
# driver.get("https://www.baidu.com/")
# driver.get_screenshot_as_file("/Users/suyayan/Downloads/driverscreen/baidus1.png")



#十八.关闭窗口
driver.get("https://www.baidu.com/")
#获得百度搜索窗口句柄
search_window=driver.current_window_handle
print('search_window:',search_window)
time.sleep(3)
driver.find_element_by_link_text("登录").click()
time.sleep(1)

#进入注册窗口
driver.find_element_by_xpath("//*[@id='passport-login-pop-dialog']/div/div/div/div[4]/a").click()
time.sleep(2)


#获得当前所有打开窗口的句柄
all_handles=driver.window_handles
print(all_handles)
time.sleep(1)


for handle in all_handles:
    if handle!=search_window:
        driver.switch_to.window(handle)
        register_window=driver.current_window_handle
        print('change to register window')
        print('close register_window')
        time.sleep(1)
        driver.close()

driver.switch_to.window(search_window) #需要把窗口句柄切回要关闭的窗口才能close它
time.sleep(1)
print('close search_window')
driver.close()


# for i in range(10):
#     driver.switch_to.window(search_window)
#     time.sleep(3)
#     driver.switch_to.window(register_window)
#     time.sleep(3)




















time.sleep(20)

driver.quit()























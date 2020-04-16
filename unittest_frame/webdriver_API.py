from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
driver=webdriver.Chrome()
driver.implicitly_wait(2)
#driver.get("https://passport.csdn.net/login")
#driver.get("https://www.baidu.com/")


'''
 一.定位元素
'''
1.通过id定位
driver.find_element_by_id('search_text')
# 动态id:auto-id
# driver.find_element_by_xpath('//*[contains(@id,"auto-id")]')
#
2.通过name定位(表单)
driver.find_element_by_name("wd").send_keys('find_element_by_name')
#
3.通过class_name定位
driver.find_elements_by_class_name("s_ipt")


4.通过link文本定位
driver.find_element_by_link_text("新闻").click()
#
5.通过link的部分文本定位
driver.find_element_by_partial_link_text("新").click()


6.通过Xpath定位百度输入框
- 绝对路径定位
# driver.find_elements_by_xpath("/html/body/div/div[2]/div/div/div/form/span/input")
-元素属性定位：//是指任意目录 ，*是指任意一个标签
# driver.find_elements_by_xpath("//*[@id='kw']")
-使用逻辑运算符
# driver.find_elements_by_xpath("//input[@id='kw' and @class='su']")
-使用文本内容匹配
#driver.find_element_by_xpath("//a[text(),"退出"]")#文本全部匹配
#driver.find_element_by_xpath("//a[contains(text(),"出")])#文本部分匹配
#
7.通过css选择器定位
 -driver.find_elements_by_css_selector(".classname/#id/tagname")

 - 通过属性定位
# driver.find_elements_by_css_selector("[name='kw']/[type='submit']")
# 组合定位:寻找一个有bg s_ipt_wr的class属性的span标签>往下一级找有class属性叫s_ipt的input标签
# driver.find_elements_by_css_selector("span.bg s_ipt_wr>input.s_ipt")

'''
二.控制浏览器
'''

1.控制浏览器窗口的大小
# driver.set_window_size(200,300)
# driver.maximize_window()

2控制浏览器后退，前进

# driver.back() #回到上一个网页
# driver.forward() #前进到上一个网页

模拟浏览器刷新
#driver.refresh()

'''
三.简单元素操作
'''
1.clear():清除文本
2.send_keys(*value)
3.click():单击元素
4.submit():提交表单


'''
四.鼠标事件
'''
#导入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains


1.context_click(): 右击
#对定位到的元素执行鼠标右键操作, perform()执行所有ActionChains中存储的行为
#action=ActionChains(driver).context_click(需要右击的元素)
# action.perform()

2.move_to_element(): 鼠标悬停
# ActionChains(driver).move_to_element（需要悬停的元素).perform()

3.double_click():  双击
# ActionChains(driver).double_click(需要双击的元素).perform()

4. drag_and_drop(source,target): 在源元素上按住鼠标左键，然后移动到目标元素上释放
# # ActionChains(driver).drag_and_drop(源元素,目标元素).perform()

'''
五.键盘事件:可以模拟键盘上的按键
'''
导入keys模块
from selenium.webdriver.common.keys import Keys

1.模拟键盘输入内容
# driver.find_element_by_id("kw").send_keys('sendkeys')
# time.sleep(2)
2.模拟键盘删除最后的一个字符
#driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

3.模拟键盘输入空格键
# time.sleep(2)
# driver.find_element_by_id("kw").send_keys(Keys.SPACE)

4.模拟键盘ctrl+a,c,v
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'c')
# driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')

5.模拟键盘回车键来代替单击操作
# driver.find_element_by_id("su").send_keys(Keys.ENTER)


'''
六.获得验证信息
'''
1.driver.title
2.driver.current_url
3.元素.text(元素标签之间的文本内容)




#七.元素等待


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#显示等待
#WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None)
#baiduinput=WebDriverWait(driver,5,0.5).until(EC.presence_of_all_elements_located((By.ID,"kw")))
#baiduinput[0].send_keys('selenium') #当我没有加[0]的时候，报错'list' object has no attribute 'send_keys'



'''
隐式等待（在创建driver之后就设置）: #在创建deriver对象之后就设置一个等待时间
'''
# 当脚本执行到某个元素定位时，如果元素可以定位，则继续执行，如果元素定位不到，则它将以轮询的方式不断地判断元素是否被定位到，超出设置时长，则抛出异常
# from selenium.common.exceptions import NoSuchElementException
 driver.implicitly_wait(5)
# driver.get("https://www.baidu.com/")
# try:
#     print(time.ctime())
#     driver.find_element_by_id("kw1").send_keys("百度隐式等待1")
# except NoSuchElementException:
#     print("没有这个元素")
# finally:
#     print(time.ctime())
#     这两个打印的时间之差就是implicitly_wait的时间
#
# driver.find_element_by_id("kw").send_keys("百度隐式等待2")


'''
八.定位一组元素:在element后面加s (返回一个数组，如果element加了s，即使只找到一个元素，也会返回数组)
'''
# driver.get("http://www.w3school.com.cn/tiy/t.asp?f=html_checkboxes")
# driver.switch_to.frame("iframeResult")  #找不到元素的时候一定要看看在不在iframe里
checkboxs=driver.find_elements_by_css_selector('input[type="checkbox"]')
checkboxs=driver.find_elements_by_xpath("//input[@type='checkbox']")
# print(checkboxs)
# for i in checkboxs:
#     i.click()


'''
 九.多frame切换:对于frame/iframe内嵌页面上的元素无法直接定位，需要通过switch_to frame()将当前定位的主体切换为frame/iframe表单的内嵌页面中
'''
# driver.switch_to.frame("frame的id，或者名字，或者索引")
# 当要再找frame之外的元素，必须切回上一层或主文档
# driver.switch_to.parent_content() 跳出当前一层表单
# driver.switch_to.default_content() 跳回最外层的页面


'''
十.多窗口切换（重要）:当在窗口1打开一个新的页面窗口2，窗口句柄（driver所指向的窗口对象）不会自动切换到新窗口2，需要switch_to，否则无法定位新窗口2的元素
'''


# 当前窗口句柄：handle1=driver.current_window_handle
# 当前所有打开窗口的句柄 ：driver.window_handles，返回一个数组。driver.window_handles[1]即是新打开的窗口2
# 切换窗口句柄：driver.switch_to.window(handle1)




'''
十一.警告框处理：switch_to.alert()定位到alert/confirm/prompt，然后使用text/accept,dismiss/send_keys等方法进行操作
'''
1.定位到警告框：
# alert=driver.switch_to.alert  (不管alert/confirm/prompt，都是switch_to.alert)
# alert.send_keys()/dismiss()/accept()


#十二.上传文件

# localfile='file://'+os.path.abspath('html_test.html')
# driver.get(localfile)
# print(localfile)
# #定位<input type='file' name='file'>这个元素，直接给这个元素send_keys文件
# driver.find_element_by_name('file').send_keys('/Users/suyayan/Downloads/pyfileoperation/signuptest.text')

#十三.下载文件
#AutoIt



'''
十四：操作cookie
'''
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




'''
十五.调用javascript
'''

# js="window.scrollTo(200,200)"  #window.scrollTo(左边距，上边距)
#js="window.scrollTo(100, document.body.scrollHeight)"
# driver.execute_script(js)

# 如果是return ,就是将取得的值返回出来
# title=driver.execute_script("return document.getElementById('bottom_footer').innerText")


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


































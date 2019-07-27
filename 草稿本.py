from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(5)

driver.get("https://www.baidu.com/")
#获得百度搜索窗口句柄


driver.find_element_by_link_text("登录").click()
#time.sleep(1)

#进入注册窗口
driver.find_element_by_xpath("//*[@id='passport-login-pop-dialog']/div/div/div/div[4]/a").click()
time.sleep(2)


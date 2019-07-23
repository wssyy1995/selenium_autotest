from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")


#通过id定位百度搜索框:
    driver.find_element_by_id("kw").send_keys("selenium2")

#通过name定位
    driver.find_element_by_name("wd").send_keys('find_element_by_name')


time.sleep(3)





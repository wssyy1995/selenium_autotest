import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('test1')
time.sleep(2)
driver.find_element_by_id('su').click()
time.sleep(2)
print(driver.title)

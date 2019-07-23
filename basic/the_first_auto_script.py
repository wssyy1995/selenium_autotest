from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

time.sleep(3)
driver.find_element_by_id("kw").send_keys("selenium2")
time.sleep(3)
driver.find_element_by_id("su").click()
time.sleep(3)





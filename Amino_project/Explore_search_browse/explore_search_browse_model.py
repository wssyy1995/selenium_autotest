import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.baidu.com")


def explore():
    driver.find_element_by_xpath()


def search(driver):
    driver.get("http://www.baidu.com")




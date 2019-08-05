import time
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver

# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("https://aminoapps.com")
#



def login_telephone(driver,username,password):
    #click sign in button
    driver.find_element_by_xpath("/html/body/header/div/div/nav/ul/li[3]/a").click()
    #click "sign in with phone"
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/button[1]").click()
    #clear data,then input username and password
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/div[1]/div/input").clear()
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/div[1]/div/input").send_keys("86")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/div[1]/input").clear()
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/input").send_keys(password)
    time.sleep(2)
    #click "sign in "
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/button").click()
    time.sleep(30)  #amino登录需要短信验证，所以只是为了测试
    # logout()


def logtestprint():
    print('start')




def logout(driver):
    driver.find_element_by_xpath("/html/body/header/div/div/nav/ul/li[3]/a/img").click()
    driver.find_element_by_xpath("/html/body/header/div/div/nav/ul/li[3]/a/div/div/div/section[1]/label/a").click()

def login_email(driver):
    driver.find_element_by_xpath("/html/body/header/div/div/nav/ul/li[3]/a").click()
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/button[2]").click()
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/div[1]/input").send_keys(username)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/input").send_keys(password)
    driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/form/button").click()
    logout()


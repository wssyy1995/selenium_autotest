import time
from selenium import webdriver
class  Log1:
    def login1(driver):
        driver.find_element_by_link_text("登录").click()
        time.sleep(1)
        driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("18221091524")
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("123456ff")
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

    def login1(driver):
        print('log out')
        usename = driver.find_element_by_xpath("//*[@id='s_username_top']/span")
        ActionChains(driver).move_to_element(usename).perform()
        driver.find_element_by_xpath('// *[ @ id = "s_user_name_menu"] / div / a[4]').click()
        driver.find_element_by_xpath("//*[@id='tip_con_wrap']/div[3]/a[3]").click()

class  Log2:
    def login2(driver,username,pwd):
        driver.find_element_by_link_text("登录").click()
        time.sleep(1)
        driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys(username)
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys(pwd)
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

    def logout2(driver):
        print('log out')
        usename = driver.find_element_by_xpath("//*[@id='s_username_top']/span")
        ActionChains(driver).move_to_element(usename).perform()
        driver.find_element_by_xpath('// *[ @ id = "s_user_name_menu"] / div / a[4]').click()
        driver.find_element_by_xpath("//*[@id='tip_con_wrap']/div[3]/a[3]").click()

class Logintest:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("http://www.baidu.com")

    def login(self,username,pwd):
        self.driver.find_element_by_link_text("登录").click()
        time.sleep(1)
        self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys(username)
        self.driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys(pwd)
        self.driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

    def logout(self):
        print('log out')
        usename = self.driver.find_element_by_xpath("//*[@id='s_username_top']/span")
        ActionChains(driver).move_to_element(usename).perform()
        self.driver.find_element_by_xpath('// *[ @ id = "s_user_name_menu"] / div / a[4]').click()
        self.driver.find_element_by_xpath("//*[@id='tip_con_wrap']/div[3]/a[3]").click()





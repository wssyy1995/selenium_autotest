import time
class  Baiduloginout:
    def bdlogin(driver):
        driver.find_element_by_link_text("登录").click()
        time.sleep(1)
        driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("18221091524")
        driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("123456ff")
        driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

    def bdlogout(driver):
        print('log out')
        usename = driver.find_element_by_xpath("//*[@id='s_username_top']/span")
        ActionChains(driver).move_to_element(usename).perform()
        driver.find_element_by_xpath('// *[ @ id = "s_user_name_menu"] / div / a[4]').click()
        driver.find_element_by_xpath("//*[@id='tip_con_wrap']/div[3]/a[3]").click()


from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)


user_data_dir = ("/Users/suyayan/Library/Application Support/Google/Chrome")
# 加载配置数据
option = webdriver.ChromeOptions()
option.add_argument(user_data_dir)
# 启动浏览器配置
driver = webdriver.Chrome(chrome_options=option,
                          executable_path="/Applications/Google Chrome.app")
driver.get("https://aminoapps.com")
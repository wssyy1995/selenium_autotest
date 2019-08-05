(1)打开chrome 显示: 您使用的是不受支持的命令行标记…
我当时的问题是由于下载的chromedriver 版本过低，可以查看chrome的版本号，下载对应的chromedriver 版本:
http://npm.taobao.org/mirrors/chromedriver/


(2)将下载好的chromedriver放到chrom 的安装目录下

（3）测试生成报告：htmltestrunner 需要放到/usr/local/lib/python3.7/site-packages


(2)smtplib.SMTPAuthenticationError: (550:
使用python发送邮件时相当于自定义客户端根据用户名和密码登录，然后使用SMTP服务发送邮件，新注册的163/126邮箱是默认不开启客户端授权的（对指定的邮箱大师客户端默认开启），因此登录总是被拒绝
解决办法（以163邮箱为例）：进入163邮箱-设置-客户端授权密码-开启（授权码是用于登录第三方邮件客户端的专用密码）



(3)每次运行一个def就会打开一个新的浏览器窗口：
解决方法：

@classmethod
def setUpClass(cls) -> None:
    cls.driver = webdriver.Chrome()
    print('start test')


    定义类setup方法，将 webdriver.Chrome()给一个类变量
    它会在所有def函数执行前，只执行一次









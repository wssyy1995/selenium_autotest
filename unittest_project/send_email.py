import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

#发送邮箱服务器
smtpserver='smtp.126.com'
#发送邮箱和密码
user='18221091524@126.com'
password='123456ffff'

#发送邮箱
sender='18221091524@126.com'
#接收邮箱
receiver='18221091524@126.com'
#发送邮件主题
subject='python email test'
#发送附件
sendfile=open('/Users/suyayan/Downloads/htmltest.html','rb').read()
#发送最新的测试报告
#定义报告的目录
result_dir='/Users/suyayan/PycharmProjects/selenium_autotest/unittest_project/baidutest'
lists=os.listdir(result_dir)
lists.sort(key=lambda fn:os.path.getmtime(result_dir+'\\'+fn))
print(('最新的文件为：'+lists[-1]))
file=os.path.join(result_dir,lists[-1])
print(file)





att=MIMEText(sendfile,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="htmltest.html"'

msgRoot=MIMEMultipart('related')
msgRoot['Subject']=subject
msgRoot.attach(att)




# msg=MIMEText('<html><h1>this is a html</h1></html>','html','utf-8')
# msg['Subject']=Header(subject,'utf-8')

#连接发送邮件
smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()

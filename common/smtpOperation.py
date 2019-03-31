import smtplib
from email.mime.text import MIMEText
from common.confOperation import getConfData
import time

from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

'''
msg_from = 'mmdd5714@163.com'
passward = 'meimei5714' #授权码
msg_to = '2418132289@qq.com'

subject = '这是测试邮件'
content = '这是用python和smtp模块发送的邮件'

msg = MIMEText(content)
msg['Subject'] = subject
msg['From'] = msg_from
msg['To'] = msg_to

try:
    s = smtplib.SMTP('smtp.163.com', 25)
    s.login(msg_from, passward)
    s.sendmail(msg_from, msg_to, msg.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print('发送失败' + format(e))
finally:
    s.quit()
'''


class Email:
    def __init__(self):
        self.msg_from = getConfData('smtpConf', 'msg_from')
        self.password = getConfData('smtpConf', 'password')
        self.msg_to = getConfData('smtpConf', 'msg_to')
        self.subject = time.strftime("%Y-%m-%d", time.localtime(time.time()))+"智能家居接口自动化测试报告"

    def send(self, filepath):
        f = open(filepath, 'rb')
        text = f.read()
        # = MIMEText(text, 'html', 'utf-8')
#        msg = MIMEText('2019-03-31_162405Example报告.html', 'html', 'utf-8')

        content = MIMEText("请查收报告。")
        message = MIMEMultipart()
        message.attach(content)
        message['From'] = Header(self.msg_from, 'utf-8')
        message['To'] = Header(self.msg_to, 'utf-8')
        subject = 'Python SMTP 邮件测试'
        message['Subject'] = Header(self.subject, 'utf-8')
        xlsx = MIMEApplication(open(filepath, 'rb').read())
        xlsx["Content-Type"] = 'application/octet-stream'
        xlsx.add_header('Content-Disposition', 'attachment', filename=filepath)

        '''
        msg['Subject'] = self.subject
        msg['From'] = self.msg_from
        msg['To'] = self.msg_to
        '''
        try:
            s = smtplib.SMTP()
            s.connect('smtp.163.com', 25)
            s.login(self.msg_from, self.password)
            s.sendmail(self.msg_from, self.msg_to, message.as_string())
            print('发送成功')
        except smtplib.SMTPException as e:
            print('发送失败' + format(e))
        finally:
            s.quit()

a = Email()
a.send(r"D:\SoftwareData\PycharmProjects\apiTestDemo\apiTestDemo\testreport\2019-03-31_192234_智能家居接口自动化测试报告.html")

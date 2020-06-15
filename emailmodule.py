import smtplib
from email.header import Header  # 用来设置邮件头和邮件主题
from email.mime.text import MIMEText  # 发送正文只包含简单文本的邮件，引入MIMEText即可
from email.mime.multipart import MIMEMultipart
import datetime

# 发件人和收件人


def mailsendrun(datetime):
    sender = 'zhuxinkai@qq.com'
    filepath = 'D:\\software\\漏洞验证工具\\CVE-2019-0708\\'
    # 所使用的用来发送邮件的SMTP服务器
    smtpServer = 'smtp.qq.com'

    # 发送邮箱的用户名和授权码（不是登录邮箱的密码）
    username = 'zhuxinkai@qq.com'
    password = 'jdceyehmcfsnbgcc'

    mail_title = '搭对巴士订票了'
    mail_body = '%s有票了去订票吧'%datetime

    msg_to = ['zhuxinkai@qq.com']
    # msg_to =['zhuxk@wyn88.com']
    # 创建一个实例
    message = MIMEMultipart()
    messagepart1 = MIMEText(mail_body, 'plain', 'utf-8')  # 邮件正文
    message['From'] = sender  # 邮件上显示的发件人
    message['To'] = ','.join(msg_to)  # 邮件上显示的收件人
    message['Subject'] = Header(mail_title, 'utf-8')  # 邮件主题

    message.attach(messagepart1)
    try:
        smtp = smtplib.SMTP_SSL(smtpServer,port=465)  # 创建一个连接
       # smtp.connect()  # 连接发送邮件的服务器
        smtp.login(username, password)  # 登录服务器
        smtp.sendmail(sender, message['To'].split(','), message.as_string())  # 填入邮件的相关信息并发送
        print("邮件发送成功！！！")
        smtp.quit()
    except smtplib.SMTPException:
        #print(smtplib.SMTPException.errno)
        print("邮件发送失败")





if __name__ == '__main__':
    mailsendrun('2020-05-11')
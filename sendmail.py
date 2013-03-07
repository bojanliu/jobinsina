#!/usr/bin/python
#coding:utf-8

import smtplib
from email.mime.text import MIMEText
import time
 
#正文
mail_body=u'叫你丫不写日报！'
#发信邮箱
mail_from='BojanLiu<lllhhw@126.com>'
#收信邮箱
mail_to=['']
#定义正文
msg=MIMEText(mail_body,_subtype='plain',_charset='gb2312')
#定义标题
msg['Subject']=u'每日日报提醒'
#定义发信人
msg['From']=mail_from
msg['To']=';'.join(mail_to)
#定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
 
smtp=smtplib.SMTP()
#连接SMTP服务器，此处用的126的SMTP服务器
smtp.connect('smtp.126.com')
#用户名密码
smtp.login('youraccount','yourpasswd')
smtp.sendmail(mail_from,mail_to,msg.as_string())
smtp.quit()
 
print 'ok'

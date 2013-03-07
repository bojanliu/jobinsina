#coding:utf-8
#filename:auto_login_pdata.py
#自动登录PDATA系统


import cookielib
import urllib2
import urllib
import re
import sys



cj=cookielib.CookieJar() #建立Cookie实例
cookies=urllib2.HTTPCookieProcessor(cj)
opener=urllib2.build_opener(cookies)#建立opener与cookie关联
urllib2.install_opener(opener)

post_url='http://cas.erp.sina.com.cn/cas/login'
data=urllib2.urlopen(post_url).read()
lt=re.findall(r"""name="lt" value="(LT-\d+?-.+?)" /""",data)
print lt[0]


header_info={'User-Agent':'Mozilla/5.0',}
post_data=urllib.urlencode({
    'username':'******',
    'password':'**********',
    'lt':lt[0],
    'ext':'null',
    })

post_url=r'http://cas.erp.sina.com.cn/cas/login?service=http://pdata.erp.sina.com.cn/login.php&ext='
req=urllib2.Request(
    url=post_url,
    headers=header_info,
    data=post_data,
    )

result=urllib2.urlopen(req)

html_source=urllib2.urlopen('http://pdata.erp.sina.com.cn/xch_v10/index.php').read()


print html_source






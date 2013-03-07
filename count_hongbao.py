#coding:utf-8
'''用于统计从主站发出的、带“#让红包飞#”关键词的原创/转发 次数/人数'''
import datetime
import pandas as pd


def main():
    f=open('c:\\result.txt','rb')
    data=f.readlines()
    f.close()

    zhuzhan_appid=('*','**','****')
    result_list=[]

    for item in data:
        item=item.split('\t')
        if item[4] in zhuzhan_appid and item[2]=='0':
            result_list.append(item[1])

    cishu=len(result_list)
    renshu=len(set(result_list))

    print u'原创次数为：%s\n原创人数为：%s'%(cishu,renshu)
    print 'OK!'
        



if __name__=='__main__':
    main()

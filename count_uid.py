#coding:utf-8
#date:20121030
"""此脚本用于查找A列表中元素在B列表中出现次数"""

import csv
import datetime


start=datetime.datetime.now()

#读取数据#
def read_data():
    f1=open('c:\\heart_uid.txt','rb').readlines()
    f2=open('c:\\uid.txt','rb').readlines()
    #转换为数值型#
    f1=[int(item) for item in f1]
    f2=[int(item) for item in f2]
    return f1,f2


def calculate(f1,f2):
    #构造字典{元素：元素次数}#
    dict_a={}
    for item in f1:
        if item in dict_a:
            dict_a[item]=dict_a[item]+1
        else:
            dict_a[item]=1

    #求出两个文件中共有的元素#
    list_a=set(dict_a.keys())
    list_b=set(f2)
    list_c=list_a&list_b

    #计算人数#
    renshu=len(list_c)

    #计算次数#
    cishu=0
    for item in list_c:
        cishu=cishu+dict_a[item]

    print u'人数为：%s\n次数为：%s'%(renshu,cishu)

    return list_c,dict_a


def create_csv(list_c,dict_a):
    #把每个元素出现次数保存为csv文件#
    f_result=open('c:\\result.csv','wb')
    writer=csv.writer(f_result)
    for item in list_c:
        writer.writerow([item,dict_a[item]])
    f_result.close()


if __name__=='__main__':
    f1,f2=read_data()
    list_c, dict_a=calculate(f1,f2)
    create_csv(list_c,dict_a)

    #打印时间#
    end=datetime.datetime.now()
    print u'运行时间为：%s'%(end-start)
    print 'ok'

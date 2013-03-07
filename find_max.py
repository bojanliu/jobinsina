#coding:utf-8
'''计算列表中元素出现个数并找出出现次数最多的前20个元素'''
import csv
import datetime

start=datetime.datetime.now()

f=open('c:\\data.txt','rb')
data=f.readlines()
f.close()

data=[item.split('\t') for item in data]
print u'数据读取OK'


result={}
i=0
for item in data:
    if item[1] in result.keys():
        result[item[1]]+=int(item[4])
    else:
        result[item[1]]=int(item[4])

    i+=1
    print '%sOK'%i

print u'汇总数据ok!'
sort=sorted(result.items(),key=lambda e:e[1], reverse=True)#字典按值排序

f=open('c:\\result.csv','wb')
writer=csv.writer(f)
for item in sort:
    writer.writerow([item[0],item[1]])
f.close()
print u'数据写入ok'

end=datetime.datetime.now()
print u'运行时间为：%s'%(end-start)
    



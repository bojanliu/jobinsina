#coding:utf-8
'''多维列表排序，找出前XX元素'''
import csv
import datetime

start=datetime.datetime.now()

f=open('c:\\yhdata.txt','rb')
data=f.readlines()
f.close()
data=[item.split('\t') for item in data]
data2=[]
for item in data:
    data2.append([item[0],int(item[1]),item[2][:-1]])
print u'数据读取OK'

data2.sort(cmp=lambda x,y:cmp(x[1],y[1]),reverse=True)




f=open('c:\\result.csv','wb')
writer=csv.writer(f)
for item in data2[:1000000]:
    writer.writerow([item[0],item[1],item[2]])
f.close()
print u'数据写入ok'

end=datetime.datetime.now()
print u'运行时间为：%s'%(end-start)
    



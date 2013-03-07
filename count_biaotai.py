#coding:utf-8
'''用于聚合表态用户的表态使用次数'''
import csv
import datetime
import pandas as pd

            
def main():
    f=open('c:\\data.txt','rb')
    data=f.readlines()
    f.close()

    data_uid=[]
    data_cishu=[]
    for item in data:
        item=item.split('\t')
        data_uid.append(item[1])
        data_cishu.append(int(item[4]))
    print u'数据读取OK'

    start=datetime.datetime.now()
    result=pd.Series(data_cishu).groupby(data_uid).sum().to_dict()
    end=datetime.datetime.now()
    print end-start
    sort_result=sorted(result.items(),key=lambda e:e[1],reverse=True)#字典按键升序排序
    print u'共有%s个用户'%len(sort_result)

    f=open('c:\\result.csv','wb')
    writer=csv.writer(f)
    for item in sort_result:
        writer.writerow([item[0],item[1]])
    f.close()
    print u'写入数据 ok'
    

    print 'all is ok'




if __name__=='__main__':
    main()

    



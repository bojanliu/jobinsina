#coding:utf-8
'''用于计算密友数、互粉数的分布情况'''
import csv
import datetime

import Queue
import threading

class DatamineThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue

    def run(self):

        while True:
            text=self.queue.get()

            #计算密友数的分布
            if text[1] in miyou_dict.keys():
                miyou_dict[text[1]]+=1
            else:
                miyou_dict[text[1]]=1
            #计算互粉数的分布
            if text[2] in hufen_dict.keys():
                hufen_dict[text[2]]+=1
            else:
                hufen_dict[text[2]]=1                

            self.queue.task_done()



            
def main():
    f=open('c:\\yhdata2.txt','rb')
    data=f.readlines()
    f.close()
    data=[item.split('\t') for item in data]
    data2=[]
    for item in data:
        data2.append([item[0],int(item[1]),int(item[2][:-1])])
    
    print u'数据读取OK'


    global miyou_dict
    global hufen_dict
    miyou_dict={}
    hufen_dict={}
    queue=Queue.Queue()

    start=datetime.datetime.now()
    for item in data2:
        queue.put(item)

    for i in range(100):
        dt=DatamineThread(queue)
        dt.setDaemon(True)
        dt.start()


    queue.join()



    sort_miyou=sorted(miyou_dict.items(),key=lambda e:e[0])#字典按键升序排序
    sort_hufen=sorted(hufen_dict.items(),key=lambda e:e[0])

    f_miyou=open('c:\\miyou.csv','wb')
    writer=csv.writer(f_miyou)
    for item in sort_miyou:
        writer.writerow([item[0],item[1]])
    f_miyou.close()
    print 'miyou is ok'

    f_hufen=open('c:\\hufen.csv','wb')
    writer=csv.writer(f_hufen)
    for item in sort_hufen:
        writer.writerow([item[0],item[1]])
    f_hufen.close()
    print 'hufen is ok'



    end=datetime.datetime.now()

    print 'all is ok'
    print end-start



if __name__=='__main__':
    main()

    



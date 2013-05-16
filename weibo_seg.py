#coding:utf-8
#filename:seg.py
#time:20130320
'''
此脚本用于对文本进行分词
'''

import jieba
import pandas as pd
import time
import Queue
import threading
import csv
import _winreg
import os




#分词
class ThreadMid(threading.Thread):
    def __init__(self, queue):
      threading.Thread.__init__(self)
      self.queue = queue

    def run(self):
      while True:
        text=self.queue.get()
        words=jieba.cut(text,cut_all=False)
        for item in words:
            result_list.append(item)
        self.queue.task_done()


#获取当前系统桌面路径
def get_desktop():
    key=_winreg.OpenKey(_winreg.HKEY_CURRENT_USER,\
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders',)
    desktop=_winreg.QueryValueEx(key, "Desktop")[0]
    return desktop


#创建结果文件
def create_csv(result_list):
    desktop=get_desktop()
    f=open(os.path.join(desktop+u'\\微博文本_'+time.strftime('%M%S')+'.csv'),'wb')
    writer=csv.writer(f)    
    for item in result_list:
        try:
            writer.writerow([item[0].encode('gb2312'),item[1]])
        except:
            writer.writerow(['writer error',item[1]])
    f.close()


def main():
    start=time.time()
    f=open('c:\\data2.txt','rb').readlines()
    #f=raw_input(u'请输入文本：').split('\n')
    end=time.time()
    print u'读取用时：%s'%(end-start)
    
    global result_list
    result_list=[]
    queue=Queue.Queue()

    start=time.time()
    for i in range(1):
        t=ThreadMid(queue)
        t.setDaemon(True)
        t.start()

    for item in f:
        queue.put(item)

    queue.join()
    end=time.time()
    print u'分词用时：%s'%(end-start)
    
    total_num=len(result_list)#总词数
    print u'结果1：总词数为%s'%total_num


    start=time.time()
    result={}
    #对列表进行groupby分组统计操作,返回一个字典
    #result=pd.Series(result_list).groupby(result_list).count().to_dict()
    for item in result_list:
        result[item]=result.get(item,0)+1
    end=time.time()
    print u'计数用时：%s'%(end-start)

    distinct_num=len(result)
    print u'结果2：排重后关键词个数为%s'%distinct_num

    start=time.time()
    #按照关键词词频倒序排序
    sort=sorted(result.items(),key=lambda e:e[1], reverse=True)
    end=time.time()
    print u'排序用时：%s'%(end-start)

    start=time.time()
    create_csv(sort)
    end=time.time()
    print u'写入用时：%s'%(end-start)
    print 'ok'
    


if __name__=='__main__':
    main()
    print 'ok'

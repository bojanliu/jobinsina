#coding:utf-8
'''对文本进行分词处理'''

from jieba import posseg as pseg


data=raw_input(u'请输入待处理文本：')
data=data.split('\n')



#分词,并给出每个词的词性
result_list=[]
for item in data:
    if item!='':
        text=pseg.cut(item)
        for item in text:
            result_list.append([item.word,item.flag])

sum_word=len(result_list)#总词数
print sum_word

#词汇频次统计，result_dict为全部分词结果集,此处结构为{词汇：[次数,词性]}
result_dict={}
for item in result_list:
    if item[0] in result_dict.keys():
        result_dict[item[0]][0]+=1
    else:
        result_dict[item[0]]=[1,item[1]]

       

#抽取出名词集
n_dict={}
for k,v in result_dict.items():
    if v[1]=='n' or v[1]=='nr' or v[1]=='v':
        n_dict[k]=v[0]

#对名词集按照出现频次对结果进行排序
sort=sorted(n_dict.items(),key=lambda e:e[1], reverse=True)

##for item in sort[:200]:
##    print item[0],item[1]

aa=[]
bb=[]
for item in sort[:50]:
    aa.append(item[0])
    bb.append(str(item[1]))

print "','".join(aa)
print ",".join(bb)
    



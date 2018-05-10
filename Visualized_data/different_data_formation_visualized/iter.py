from itertools import groupby
from  itertools import *

#测试itertools工具中groupby功能
#返回 key[分组名]，group[同名组]

qs=[{"date":1},{"date":2}]
#例1
for key,g in groupby("aaaabbbcccd"):
    print(key,list(g))
#例2
for name,group in groupby(qs,lambda x:x["date"]):
    print(name,list(group))      #函数值+分组

#例3
a=["a","f","aa","bb","ccc","eee"]
lst=[(length,list(group)) for length,group in groupby(a,len)]
print(lst)
for length,group in groupby(a,len):
    print(length,list(group))

#其他itertools工具
lst1=dropwhile(lambda x:x<5,range(10))
lst2=takewhile(lambda x:x<7,range(10))
print(list(lst1))
print(list(lst2))
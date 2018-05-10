from itertools import groupby
#help(zip)
x_date=[1,1,1,2,2,2]
y_date=[1,2,3,4,5,6]
xy_map=[]
zl=zip(x_date,y_date)
print(list(zl))
zsl=sorted(zip(x_date,y_date))
print(zsl)
obj1=groupby(sorted(zip(x_date,y_date)),key=lambda _:_[0])
for x,y in obj1:
    print(x,list(y))

for x,y in groupby(sorted(zip(x_date,y_date)),key=lambda _:_[0]):
    #print(list(y))
    #以元组（m,n）接受y列表中的元组
    #for m,n in y:
        #print(m,n)
    y_list=[v for _,v in y]
    #print(y_list,end="")
    xy_map.append([x,sum(y_list)/len(y_list)])
print(xy_map)
print(*xy_map)
print(list(zip(*xy_map)))
print(*zip(*xy_map))
x_unique,y_mean=[*zip(*xy_map)]
print(x_unique,y_mean)

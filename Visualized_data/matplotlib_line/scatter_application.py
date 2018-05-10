import matplotlib.pyplot as plt
#可视化数据 matplotlib.pyplot散点图运用运用

help(plt.cm)

#列表存储数据
#x_values=[1,2,3,4,5]
#y_values=[1,4,9,16,25]

#自动计算数据
x_values=list(range(1,1001))
y_values=[x*x for x in x_values]

#可视化数据
plt.scatter(x_values,y_values,s=5,c=y_values,cmap=plt.cm.Blues)
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of value",fontsize=14)
plt.axis([0,1100,0,1100000])
plt.show()
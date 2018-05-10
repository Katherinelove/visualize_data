import matplotlib.pyplot as plt

#可视化数据 matplotlib.pyplot折现图运用
help(plt.tick_params)

#存储数据
squares=[1,4,9,16,25]
input_values=[1,2,3,4,5]

#可视化数据
plt.plot(input_values,squares,linewidth=2,color="green")               #提供输入输出值作为校正
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14,color=(0,0,0.8))
plt.ylabel("square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14,colors="gold",direction="inout",
                width=2,left=False,right=True,labelleft=False,labelright=True,pad=5)
plt.show()

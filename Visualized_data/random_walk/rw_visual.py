from random_walk import Random_walk
import matplotlib.pyplot as plt

while True:
    rw = Random_walk(10000)
    rw.fill_walk()
    #设置绘制窗口大小
    plt.figure(figsize=(10,6),facecolor="gray")
    point_number=list(range(rw.num_point))
    #c=list 和cmap必须一起连用才能生效
    plt.scatter(rw.x_values, rw.y_values, s=5, c=point_number,cmap=plt.cm.Blues)
    #突出起点和终点
    plt.scatter(0,0,s=20,c="green")
    plt.scatter(rw.x_values[-1],rw.y_values[-1],s=20,c="red")
    #隐藏坐标轴
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()
    keep_running=input("Make another walk?(y/n):")
    if keep_running.strip().lower()[0]=="n":
        break
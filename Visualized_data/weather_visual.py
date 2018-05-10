import csv
from datetime import datetime
import matplotlib.pyplot as plt

#分析文件头
filename="sitka_weather_2014.csv"
with open(filename) as f:
    reader=csv.reader(f)     #得到的reader是一个iterator
    header_row=next(reader)
    #查看所有数据
    #for val in reader:
    #    print(val)
#读取并存储数据,
    dates,highs_collumn,lows_collumn=[],[],[]


    for row in reader:
        date=datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(date)
        high=int(float(row[1]))
        highs_collumn.append(high)
        low=int(float(row[3]))
        lows_collumn.append(low)


#绘制折线图
plt.figure(figsize=(10,6))

plt.plot(dates,highs_collumn,c="red")
plt.plot(dates,lows_collumn,c="green")
plt.fill_between(dates,highs_collumn,lows_collumn,facecolor="blue",alpha=0.1)
plt.title("delta of temperature",fontsize=24)
plt.xlabel("",fontsize=16)
#fig.autofmt_xdate()          #绘制倾斜的x标签
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis="both",labelsize=16)

plt.show()
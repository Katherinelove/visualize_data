from urllib.request import urlopen

import json
import pygal
import math


#利用API获取数据，并下载数据
json_url="https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
response=urlopen(json_url)

#读取数据
read=response.read()
#写入数据（即下载数据）
with open("btc_close_2017.json","wb") as f:
    f.write(read)
#打开数据
with open("btc_close_2017.json") as f:
    local_file=json.load(f)
#读取全部数据
    #for value in local_file:
    #print(value)

#创建5个列表 存储相应的数据
dates=[]
months=[]
weeks=[]
weekdays=[]
close=[]

for btc_dict in local_file:
    dates.append(btc_dict["date"])
    months.append(int(btc_dict["month"]))
    weeks.append(int(btc_dict["week"]))
    weekdays.append(btc_dict["weekday"])
    close.append(int(float(btc_dict["close"])))

#pygal可视化数据(折现图)
line_chart=pygal.Line(x_label_rotation=30,show_minor_x_labels=False)
line_chart.title="收盘价"
line_chart.x_labels=dates
N=20     #x坐标每隔20天显示一次
line_chart.x_labels_major=dates[::N]
line_chart.add("收盘价",close)
line_chart.render_to_file("收盘价折现图（￥）.svg")
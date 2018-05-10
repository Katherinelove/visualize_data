from urllib.request import urlopen
import json
from itertools import groupby
import pygal
import math

#获取数据
json_url="https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json"
responsee=urlopen(json_url)

#读取数据
read=responsee.read()
#写入数据
with open("btc_close_2017.json","wb") as f:
    f.write(read)

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
#对数变换
close_log=[math.log10(_) for _ in close]
line_chart.add("收盘价",close_log)
line_chart.render_to_file("收盘价对数变换折现图（￥）.svg")


def draw_line(x_date,y_date,title,y_legend):
    xy_map=[]
    for x,y in groupby(sorted(zip(x_date,y_date)),lambda _:_[0]):
        y_list=[v for _,v in y]
        xy_map.append([x,sum(y_list)/len(y_list)])
    x_unique,y_mean=[*zip(*xy_map)]
    line_chart=pygal.Line()
    line_chart.title=title
    line_chart.x_labels=x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+".svg")
    return line_chart


idx_month=dates.index("2017-12-01")            #2017-12数据不完整，将十二月的天数切片去除
line_chart_month=draw_line(months[:idx_month],close[:idx_month],"收盘价月日均值（￥）","月日均值")
idx_week=dates.index("2017-12-11")             #2017-01-01为上年的周日切片去掉，2017-12-10位2017年49周周日
line_chart_week=draw_line(weeks[1:idx_week],close[1:idx_week],"收盘价周日均值（￥）","周日均值")   #切片工具也是左包右不包


#为了绘制每周具体的日均值
wd=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#通过wd中的英文索引  提取对应一周的1-7
weekdays_int=[wd.index(w)+1 for w in weekdays[1:idx_week]]
line_chart_weekday=draw_line(weekdays_int,close[1:idx_week],"收盘价星期均值（￥）","星期均值")
#修改坐标
line_chart_weekday.x_labels=["周一","周二","周三","周四","周五","周六","周日"]
#修改后必须再重新输出
line_chart_weekday.render_to_file("收盘价星期均值（￥）.svg")


#将几张图写在一个web界面  利用Html5
with open("收盘价Dashboard.html","w",encoding="utf8") as html_file:
    html_file.write('<html><head><title>收盘价Dashboard.html</title><meta charset="utf-8"></head><body>\n')
    for svg in ["收盘价折现图（￥）.svg","收盘价对数变换折现图（￥）.svg","收盘价月日均值（￥）.svg",
                "收盘价周日均值（￥）.svg","收盘价星期均值（￥）.svg"]:
        html_file.write('<object type="image/svg+xml" data="{0}" width=500></object>\n'.format(svg))
    html_file.write("</body></html>")
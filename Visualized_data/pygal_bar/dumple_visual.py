from pygal_bar.die import Die
import pygal

#创建两个D6骰子
die_1=Die()
die_2=Die()

#获取实验数据
results=[]
for roll_num in range(1000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

#分析数据
frequences=[]
for value in range(2,die_1.num_sides+die_2.num_sides):
    frequent=results.count(value)
    frequences.append(frequent)

#可视化结果
hist=pygal.Bar()

hist.title="Results of rolling two D6 dice 1000 times."
#hist.x_labels=[str(i) for i in range(2,13)]
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12']
hist._x_title="Result"
hist._y_title="Frequence of Result"

#添加并输出数据
hist.add("D6+D6",frequences)
hist.render_to_file("dumple_visuak.svg")
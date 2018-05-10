import pygal
from pygal_bar.die import Die

#创建一个D6(默认为6)
die=Die()
#存储数据
results=[]
for roll_num in range(1000):
    result=die.roll()
    results.append(result)
#分析结果
frequencies=[]
for value in range(1,die.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
hist=pygal.Bar()
hist.title="Results of rolling one D6 100 times."
hist.x_labels=[1,2,3,4,5,6]
hist._x_title="Result"
hist._y_title="Frequency of Result"

hist.add("D6",frequencies)
hist.render_to_file("die_visual.svg")

# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [340, 179, 98, 294, 266]
plt.style.use('ggplot')
group_labels = ['BeiJing', 'Shanghai','Guangzhou','Chengdu','Shenyang']
plt.bar(x, y, color='rgb', alpha=0.3)
plt.xticks(x, group_labels, rotation=0)
plt.xlabel('City Name')
plt.ylabel('Days')
plt.title('Five City Comparision')
plt.show()
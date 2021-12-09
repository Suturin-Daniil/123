from matplotlib import markers
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import size

fig, ax = plt.subplots() # axes - пространство, в котором будут создаватья графики
ax.plot([1,2,3,4], [1,4,9,16]) # задади ломанную
plt.show()


x = np.linspace(0, 4, 40)
y = np.linspace(0, 4, 50)
fig, ax1 = plt.subplots()
ax1.scatter(2, 40, marker = '*')
ax1.scatter(x, x**2, label = 'quadratic', marker='+', linewidths = 1, color = 'r', s = 30) # задади параболу, scatter позволит построить по точкам
ax1.plot(y, y**3, label = 'cubic', marker = 'o') # задади кубическую параболу, plot соединяет точки из массива данных y
# метка label позволит нанести название графика в легенду
# marker позволяет добавить вид точек графика
# linewidths определяет толщину линии
# color устанавливает цвет линии
# s позволяет установить размер маркера, НО только в методе scatter
ax1.legend() # добавляем легенду
ax1.set_xlabel('x label') # добавим подписи осей
ax1.set_ylabel('y label')
ax1.set_title('easy graph') # добавим название графика
plt.show()
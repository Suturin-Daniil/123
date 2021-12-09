import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np
import math
d40 = np.loadtxt("стоячая вода 40 mm (15 s).txt", dtype=int) # c помощью np.loadtxt считываем данные из файлов в массивы
d60 = np.loadtxt("стоячая вода 60 mm (15 s).txt", dtype=int) # dtype - указываем тип данных, которые будет содержать массив
d80 = np.loadtxt("стоячая вода 80 mm (15s).txt", dtype=int)
d100 = np.loadtxt("cстоячая вода 100мм (12s).txt", dtype=int)
d120 = np.loadtxt("Стоячая вода 120 mm (15s).txt", dtype=int)

d = [d40, d60, d80, d100, d120] # отдельный массив массивов с отсчетами АЦП из файлов
h = [40, 60, 80, 100, 120] # массив уровней воды в мм
a = []

for i in range(5):       # циклом добавляем в массив a средние значения отсчетов АЦП из массивов d40 - d120
    a.append(np.mean(d[i])) # усредняем с помощью функии np.mean, которая возвращает среднее значение из набора данных
                            # можем так делать, т. к. вода стоячая и отсчеты АЦП характерезуют одно состояние
fig, ax = plt.subplots()
plt.plot(h, a, '+', color = 'r', label = 'измерения') # наносим на график точки(среднее значения отсчетов АЦП и соответствующий уровень воды)

p = np.polyfit(a, h, 50) # с помощью polyfit по полученным точкам ищем зависимость, которая максимально ложитсяя на точки, 50 - это степень многочлена, которым интерполируем точки
al = np.linspace(int(np.mean(d40)), int(np.mean(d120)), int(np.mean(d120)-np.mean(d40)+1)) # создаем массив отсчетов ацп от 40 до 120
hl = np.polyval(p, al) # с помощью polyval получаем значения функции, которую вывели через polyfit, то есть переводим отсчеты АЦП в уровень воды

ax.set_xlabel('Уровень воды [мм]') # ниже просто строим график калибровочный
ax.set_ylabel('Отсчёты АЦП')
ax.set_title('Калибровочный график зависимости \n показаний АЦП от уровня воды')

plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='green', linestyle='--', linewidth = 0.25)

print(p)

plt.plot(hl, al, label = 'линия интерполяции')
ax.legend()
plt.savefig('kalibrovka.png')

#------------------------------------------------------------------------------------------------
#_____________________________________________________________________________________________


data40 = np.loadtxt("40mm (10 s).txt", dtype = int, skiprows = 15094)  # из текстовых файлов считываем в массивы отсчеты АЦП при открытой дверце

data80 = np.loadtxt("80 MM (10S).txt", dtype = int, skiprows = 30003)

data120 = np.loadtxt("120 mm (15s).txt", dtype = int)

data40 = np.polyval(p, data40) # используем функцию p, которую через polyfit вывели выше, для перевода отсчетов АЦП в уровень воды 

data80 = np.polyval(p, data80)

data120 = np.polyval(p, data120)

t40 = np.linspace(0, 10, len(data40)) # создаем массив времен размером массивов уровней воды

t80 = np.linspace(0, 10, len(data80)) # чтобы массивы были одинаков размеров и графики четко строились

t120 = np.linspace(0, 15, len(data120))

#---------------------------------------------

# fig, ax40 = plt.subplots()
# ax40.plot(t40, data40)

# plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
# plt.grid(which='minor', color='green', linestyle='--', linewidth = 0.25)

# plt.xlim(0, 12)
# plt.show()

#-----------------------------------------------

fig, ax80 = plt.subplots() # строим график зависимости уровня воды от времени
ax80.plot(t80, data80)

ax80.plot([0.5, 0.5, 0.5], np.linspace(0, 100, 3), color = 'r', marker = '_')

plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='green', linestyle='--', linewidth = 0.25)

ax80.set_xlabel('Время [с]')
ax80.set_ylabel('Уровень воды [мм]')
ax80.set_title('Уровень воды в кювете \n после открытия торцевой двери')

box_1 = {'facecolor':'white',  # создаем участок на графике где поместим данные о времени и скорости
       'edgecolor': 'black',     
       'boxstyle': 'round'}    

ax80.text(2, 80, 'L = 1,47 [м] \n t = 0,5 [с] \n V = 2,94 [м/с]', Bbox = box_1, fontsize = 15) # добавляем в область скорость, время, расстояние от дверцы до электродов

plt.xlim(0, 4)
plt.ylim(30, 100)
fig.savefig("80mm.png")
plt.show()

#--------------------------------------------------------------------

fig, ax120 = plt.subplots() # то же самое делаем олько для 120 mm
ax120.plot(t120, data120)

ax120.plot([1.25, 1.25, 1.25], np.linspace(0, 130, 3), color = 'r', marker = '.')

plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='green', linestyle='--', linewidth = 0.25)

ax120.set_xlabel('Время [с]')
ax120.set_ylabel('Уровень воды [мм]')
ax120.set_title('Уровень воды в кювете \n после открытия торцевой двери')

box_2 = {'facecolor':'white',   
       'edgecolor': 'black',     
       'boxstyle': 'round'} 

ax120.text(2.5, 110, 'L = 1,47 [м] \n t = 1,25 [с] \n V = 1.176 [м/с]', Bbox = box_2, fontsize = 15)


plt.xlim(0, 4)
plt.ylim(40, 130)
fig.savefig("120mm.png")
plt.show()




from waveFunctions import *
import numpy as np
import matplotlib.pyplot as plt

path = '/home/gr102/Desktop/Лабораторная работа/'

data20, duration, count = readWaveData(path + '40.txt')
data40, duration, count = readWaveData(path + '60.txt')
data60, duration, count = readWaveData(path + '80.txt')
data80, duration, count = readWaveData('.txt')
data100, duration, count = readWaveData('cстоячая вода 100мм (12s).txt')
data120, duration, count = readWaveData('стоячая вода 120 mm (15s).txt')

heights = [40, 60, 80, 100, 120]
adc = [np.mean(data40), np.mean(data60), np.mean(data80), np.mean(data100), np.mean(data120)]

plt.title('Калибровочный график')
plt.xlabel(u'h, mm')
plt.ylabel(u'adc')
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)

adclist=np.linspace(np.mean(data40),np.mean(data120),int(np.mean(data120)-np.mean(data40)))
p = np.polyfit(adc, heights, 2)
h=[]
for i in range(int(np.mean(data40)),int(np.mean(data120))):
    h.append(np.polyval(p,i))
plt.plot(h,adclist)
plt.show()

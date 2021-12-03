import matplotlib.pyplot as plt
import numpy as np
import math
d40 = np.loadtxt("стоячая вода 40 mm (15 s).txt", dtype=int)
d60 = np.loadtxt("стоячая вода 60 mm (15 s).txt", dtype=int)
d80 = np.loadtxt("стоячая вода 80 mm (15s).txt", dtype=int)
d100 = np.loadtxt("cстоячая вода 100мм (12s).txt", dtype=int)
d120 = np.loadtxt("Стоячая вода 120 mm (15s).txt", dtype=int)
d = [d40, d60, d80, d100, d120]
h = [40, 60, 80, 100, 120]
a = []
for i in range(5):
    a.append(np.mean(d[i]))
 
fig, ax = plt.subplots(figsize=(16,10), dpi=400)
plt.plot(h, a, '+')

p = np.polyfit(a, h, 2)
al = np.linspace(int(np.mean(d40)), int(np.mean(d120)), int(np.mean(d120)-np.mean(d40)+1))
hl = np.polyval(p, al)
plt.plot(hl, al)

 
 
 
 
plt.title("Калибровочный график зависимости показаний АЦП от уровня воды", fontstyle = 'italic', horizontalalignment = 'center')
plt.xlabel("Уровень воды, мм")
plt.ylabel("Отсчёты АЦП")
 
ax.plot()
plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', color='green', linestyle='--', linewidth = 0.25)
 
ax.set_xlim([min(h), 1.1*max(h)])
ax.set_ylim([min(a), 1.1*max(a)])

 
plt.minorticks_on()
 
fig.savefig("level-calibration.png")
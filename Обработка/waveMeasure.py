from waveFunctions import *

import spidev
import time
import RPi.GPIO as GPIO
import numpy as np
import matplotlib.pyplot as plt

spi = spidev.SpiDev()

initSpiAdc()



waitForOpen()

data = []
c = 0

T1 = time.perf_counter()

while (time.perf_counter() - T1 <= 15):
    data.append(getAdc())
    c += 1

T2 = time.perf_counter()

save(data, T1, T2)
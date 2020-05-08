import numpy as np
import matplotlib.pyplot as plt
import math
from random import random

def f(x):
    if x == 0:
        return 0
    else:
        y = x**(-1/4)/(np.exp(x)+2)
        return y

Ntest = 1000
N = 10
a = 0.0
b = 1.0
counter = 0

all_mean = []
all_SD = []
all_SE = []

for k in range(Ntest):

    all_x = []

    for h in range(N):
        x = a+(b-a)*random()
        all_x.append(x)

    sum_x = 0
    for i in range(N):
        sum_x += f(all_x[i])

    mean_x = sum_x/N

    sum_x2 = 0

    for j in range(N):
        sum_x2 += (f(all_x[j])-mean_x)**2

    SD_x = (sum_x2/(N-1))**0.5
    SE_x = SD_x/(N**0.5)

    all_mean.append(mean_x)
    all_SD.append(SD_x)
    all_SE.append(SE_x)

    if abs(mean_x-0.3763210604753777) < SE_x:
        counter += 1

avg = 0
for i in range(len(all_mean)):
    avg += (b-a)*all_mean[i]

I = (b-a)*avg/Ntest

print("SE_x: ",SE_x)
print("Mean value method to calculate the integral: ",I)
print('Confidence Interval (theoretical value = 0.68): %6.4f'%(counter/Ntest))
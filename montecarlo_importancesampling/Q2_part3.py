import numpy as np
import matplotlib.pyplot as plt
import math
import time
import random


Num = 10**4
N_b = 10**2
mu1 = 0
mu2 = 1
sigma1 = 0.5
sigma2 = 0.3

# get weight
def get_weight(x):
    return np.exp(-(x - mu1) ** 2 / (2 * sigma1 ** 2)) + np.exp(-(x - mu2) ** 2 / (2 * sigma2 ** 2))

# equation given
def ff(x):
    y = x**(-1/4)/(np.exp(x)+2)
    return(y)
xmax = 1
xmin = 0
arr_x = np.zeros([N_b * Num])
arr_g = np.zeros([N_b])
# randomly picked configuration
x0 = np.random.random()

ntp = 0
for nb in range(N_b):
    tmp = 0
    # repeat for 'Num' repetitions 
    for ns in range(Num):
        x1 = np.random.random()
        # examining whether to accept trial configuration by comapring with trasition matrix
        if get_weight(x1) / get_weight(x0) > np.random.random():
            arr_x[ntp] = x1
        else:
            arr_x[ntp] = x0
        x0 = arr_x[ntp]
        ntp += 1
        tmp += ff(x0)

    arr_g[nb] = tmp / Num

var_g = np.var(arr_g)
mean_g = np.mean(arr_g)
error_g = np.sqrt(var_g / (N_b - 1))

print("Computation Time: ", time.process_time())

print("Results: ", mean_g, " Error: ", error_g)

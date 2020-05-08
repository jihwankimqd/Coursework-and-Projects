import numpy as np
import matplotlib.pyplot as plt
import math
import random

# When Num = 10, the confidence interval d3 (0.99) can be acheived. But when Num increases,
# the accuracy of the result increases, but the confidence interval decreases. 
Num = 1000
N_b = 10
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


counter = 0

for i in range(Num):
    ntp = 0
    for nb in range(N_b):
        tmp = 0
        # repeat for 'Num' repetitions 
        # for ns in range(Num):
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
        # SD = var_g**0.5
        # SE = SD/(N_b**0.5)
        mean_g = np.mean(arr_g)
        error_g = np.sqrt(var_g / (N_b - 1))

    if abs(mean_g-0.3763210604753777) < 3*error_g:
    # if abs(mean_g-0.3763210604753777) < 3*SE:
        counter += 1


print("Confidence Interval using Importance Sampling (Theoretical Value = 0.99): ", counter/Num)

print("Results: ", mean_g, " Error: ", error_g)

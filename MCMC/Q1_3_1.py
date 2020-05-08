import numpy as np
import matplotlib.pyplot as plt
import math
from random import random

# given equation
def f(x):
    y = x**(-1/4)/(np.exp(x)+2)
    return y

# equation to transform 
def g(z):
    x = z**(4/3)
    y = 4/  (np.exp(x) + 2) /3
    return(y)

# using mean value method
Num = 1000
N_b = 1000
arr1 = []
arr2 = []
X_total = []
counter = 0
for i in range(N_b):
    x_rand = np.random.random(Num)
    wx = x_rand**(4/3)
    x_total = X_total + list(x_rand)
    wx_total = X_total + list(wx)
    total1 = np.sum(f(x_rand))
    total2 = np.sum(g(x_rand))
    ans1 = total1/Num
    arr1.append(ans1)
    ans2 = total2/Num
    arr2.append(ans2)



    # sum2 = 0
    # for i in range(len(x_rand)):
    #     sum2 += (g(x_rand)-ans2)**2
    # print("Sum: ",sum2)
    # SD = (sum2/(N_b-1))**0.5
    # SE = SD/(N_b**0.5)
#     if abs(ans2-0.3763210604753777) < 2*SE:
#         counter += 1


Ntest = Num
N = N_b
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
        sum_x += g(all_x[i])

    mean_x = sum_x/N

    sum_x2 = 0

    for j in range(N):
        sum_x2 += (g(all_x[j])-mean_x)**2

    SD_x = (sum_x2/(N-1))**0.5
    SE_x = SD_x/(N**0.5)

    all_mean.append(mean_x)
    all_SD.append(SD_x)
    all_SE.append(SE_x)

    # 2 * SE_x because it is in the confidence interval d2
    if abs(mean_x-0.3763210604753777) < 2*SE_x:
        counter += 1

print("Error: ",SE_x)

print("Confidence Interval using Importance Sampling (Theoretical Value = 0.95): ", counter/Num)

# plt.figure(1,figsize = (13,7))
# plt.subplot(231).set_title('Uniform Random Number')
# plt.hist(x_total,bins = 50)
# plt.subplot(232).set_title('Ordinary Mean Value Method')
# plt.plot(np.linspace(0,N_b,len(arr1)),arr1,'*')
# plt.subplot(233).set_title('Historgram Using Ordinary Mean Value Method')
# plt.hist(arr1,bins = 50)
# plt.subplot(234).set_title('Non-Uniform Random Number')
# plt.hist(wx_total,bins = 50)
# plt.subplot(235).set_title('Mean Value Method with Importance Sampling')
# plt.plot(np.linspace(0,N_b,len(arr2)),arr2,'*')
# plt.subplot(236).set_title('Uniform Random Number')
# plt.hist(arr2,bins = 50)
# plt.show()

print("Results with Importance Sampling: ", np.sum(arr2)/N_b)


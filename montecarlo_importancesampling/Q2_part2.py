import numpy as np
import matplotlib.pyplot as plt
import math
import random

# given equation
def f(x):
    y = x**(-1/4)/(np.exp(x)+2)
    return y

# equation to transform 
def g(z):
    x = z**(4/3)
    y = 4/  (np.exp(x) + 2) /3
    return(y)

# using mena value method
Num = 10**5
N_b = 10**3
arr1 = []
arr2 = []
X_total = []
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

plt.figure(1,figsize = (13,7))
plt.subplot(231).set_title('Uniform Random Number')
plt.hist(x_total,bins = 50)
plt.subplot(232).set_title('Ordinary Mean Value Method')
plt.plot(np.linspace(0,N_b,len(arr1)),arr1,'*')
plt.subplot(233).set_title('Historgram Using Ordinary Mean Value Method')
plt.hist(arr1,bins = 50)
plt.subplot(234).set_title('Non-Uniform Random Number')
plt.hist(wx_total,bins = 50)
plt.subplot(235).set_title('Mean Value Method with Importance Sampling')
plt.plot(np.linspace(0,N_b,len(arr2)),arr2,'*')
plt.subplot(236).set_title('Uniform Random Number')
plt.hist(arr2,bins = 50)
plt.show()
print(np.sum(arr1)/N_b,np.sum(arr2)/N_b)


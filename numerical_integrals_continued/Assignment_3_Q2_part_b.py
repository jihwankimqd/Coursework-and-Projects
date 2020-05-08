import numpy as np
import matplotlib.pyplot as plt
import math
import time
from gaussxw import gaussxwab


# tried to find the value of c such that the function is at its maximum when z = 0.5
N = 10000
a = 6

# c = 6 when z=0.5 is maximum (found out through helper function below)
c = 1

# c = 1 is the second part of part b
# c = 1

# c is closest to the analytical result of 120 when c = 6.50, where it returns 120.00000000000001
# c = 6.50

x_array = []
y_array = []


# def f(z):
#     x = c*z/(1-z)
#     y =  (x**(a-1))*(np.e**(-x))
#     dxdz = c/((1-z)**2)
#     return (y*dxdz)

def f(z):
    i = ((c*z)/(1-z))**(a-1)
    j = np.exp(-(c*z)/(1-z))
    k = c/((1-z)**2)
    return i*j*k

# print(f(0.))

# for i in range(N):
#     x_array.append(i)
x_array = np.linspace(0.000000001,.999999999,N)
# print(x_array)

for i in range(len(x_array)):
    # print('i: ', i)
    y_array.append(f(x_array[i]))

# helper function to see if the maximum value of the function is at z=0.5
def findbiggestelement(array):
    largest = 0
    position = 0
    for i in range(len(array)):
        if array[i] > largest:
            largest = array[i]
            position = i
    return largest, position

# print(findbiggestelement(y_array))
# below returns 0.499949994999 which is close to z=0.5
# print(x_array[4999])

plt.figure()
plt.title('Gamma Function Conversion Method c = 1')
plt.plot(x_array,y_array)
plt.xlabel('z')
plt.ylabel('f(z)')
axes = plt.gca()
axes.set_xlim([0,1])
axes.set_ylim([None,None])
plt.legend()
plt.show()

lower = 0.0
upper = 1.0
x,w = gaussxwab(N,lower,upper)
s = 0.0
for i in range(N):
    s += w[i]*f(x[i])
print(s)




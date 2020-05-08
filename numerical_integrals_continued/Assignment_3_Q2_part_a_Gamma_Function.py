import numpy as np
import matplotlib.pyplot as plt
import math
import time


# a = 0.0
# b = 2.0

N = 8
a = 0

def f(x):
    return (x**(a-1))*(np.e**(-x))

x = []
for i in range(N+1):
    x.append(i)

    
# when a=2
a = 2
x_a2 = x
y_a2 = []

for i in range(len(x_a2)):
    y_a2.append(f(i)) 


# when a=3
a = 3
x_a3 = x
y_a3 = []

for i in range(len(x_a3)):
    y_a3.append(f(i)) 

# when a=4
a = 4
x_a4 = x
y_a4 = []

for i in range(len(x_a4)):
    y_a4.append(f(i)) 

plt.figure()
plt.title('Gamma Function')
plt.plot(x_a2,y_a2,'*-r', label = 'a=2')
plt.plot(x_a3,y_a3,'*-g', label = 'a=3')
plt.plot(x_a4,y_a4,'*-b', label = 'a=4')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()

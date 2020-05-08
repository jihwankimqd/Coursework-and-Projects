import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math
import time

#run your code

def f(x):
    if x == 0:
        return(0)
    else:
        return (np.cos(x)- 2*(np.sin(x)))/(np.sqrt(x))

# for gaussian quad method, because the if x==0 statement causes an error
def g(x):
    return (np.cos(x)- 2*(np.sin(x)))/(np.sqrt(x))

# N = 1000000
a = 0.0
b = 1.0

# a_new to address singularities in the integral
a_new = a+ 0.000000001

# 5) Gaussian Quadrature
from gaussxw import gaussxwab

accuracy = 1e-3

n = 10

def gaussian(f, a, b, n=n):
    # removes ambiguity error with gauss method
    f = g

    x, w = gaussxwab(n, a, b)

    # while(error > accuracy):
    #     n = n*2
    #     x, w = gaussxwab(n, a, b)
    #     print(n)
    #     print(error)
    return sum(f(x) * w)
# print("Gaussian Quadrature Method: ", gaussian(f,a,b))

gaussian(f,a,b)
# print(quad(f,a,b))

# error array 
e = []
# result array
r = []
# slices array
slices = []
# for plotting graph
x = []
y = []

error = 0.5679752689070126-gaussian(f,a,b)
while(error > accuracy):
    n = n*2
    # print(n)
    error = 0.5679752689070126-gaussian(f,a,b,n)
    x.append(math.log(n/2,2))
    y.append(math.log(error,10))
    e.append(error)
    slices.append(n)
    r.append(gaussian(f,a,b,n))

for i in range(len(e)):
    print("Gaussian Quadrature: ", r[i], "Error: ", e[i], "Slices: ", slices[i])


# print("Comparison with the Scipy Quad Function")
# print("Scipy Integration: ", quad(f,a,b), "Gaussian Quadrature: ", gaussian(f,a,b), "Error: ", error, "Slices: ", n)

print("Computation Time: ", time.process_time())


plt.figure()
plt.title('This is the Gaussian Quadrature results')
plt.plot(x,y,'*-')
plt.xlabel(r'$log_2(n/10)$')
plt.xlim(0,max(x))
plt.ylabel(r'$log_{10}(Integral_Result)$')
plt.show()


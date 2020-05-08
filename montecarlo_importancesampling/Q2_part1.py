import numpy as np
import matplotlib.pyplot as plt
import math
import random

def f(x):
    if x == 0:
        return 0
    else:
        y = x**(-1/4)/(np.exp(x)+2)
        return y


N = 2
a = 0.0
b = 1.0

# Adaptive Trapezoidal Rule

def trapezoidal(N):
    h = (b-a)/N
    s = 0.5*f(a) + 0.5*f(b)
    for i in range(1,N):
        s = s + f(a+(i*h))
    s = s*h
    return s
# print("trap: ", trapezoidal(N))

# Helper function calculating adaptive method to calculate the odd steps of the integral.
def adaptive(N):
    h = (b-a)/N
    s = 0
    for i in range(1, N, 2):
        s += f(a+(i*h))
    s = s*h
    return s
# print("adap: ", adaptive(N))


# error array 
e = []
# result array
r = []
# slices array
slices = []
# for plotting graph
x = []
y = []

def adaptive_trapezoidal(N):
    error = 1
    accuracy = 1.0e-4
    s = trapezoidal(N)
    s_old = s
    while error > accuracy:
        N = N*2
        s = s_old/2.0 + adaptive(N)
        error = abs(s-s_old)/3.0
        s_old = s
        # print(error)
        # print(N)
        # print(error)
        x.append(math.log(N/2,2))
        y.append(math.log(error,10))
        e.append(error)
        r.append(s)
        slices.append(N)
    # return(s)
    return

adaptive_trapezoidal(N)

for i in range(0, len(e)):
    print(i,"th Error: ", e[i],"Result: ", r[i], "Slices: ", slices[i])
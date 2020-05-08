import numpy as np
import matplotlib.pyplot as plt
import math

# def weierstrass(x):
def f(x):
    result = 0
    for i in range(0,101):
        result += (a**i)*(np.cos((b**i)*np.pi*x))
    return result

N = 2
a = 0.0
b = 0.5

# a_new to address singularities in the integral
a_new = a+ 0.000000001
# # 2) Adaptive Trapezoidal Rule
# # Since the adaptive trapezoidal needs the integral value of the (i-1)th integral,
# # it should be coded too

# # Trapezoidal method written with reference to the formula

def trapezoidal(N):
    h = (b-a_new)/N
    s = 0.5*f(a_new) + 0.5*f(b)
    for i in range(1,N):
        s = s + f(a_new+(i*h))
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
    # anything more accurate than 1.0e-4 will take too long to compute
    accuracy = 1.0e-5
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
    return s

adaptive_trapezoidal(N)

# for i in range(0, len(e)):
#     print(i,"th Error: ", e[i],"Result: ", r[i], "Slices: ", slices[i])

# # print("Adaptive Trapezoidal Rule: ", adaptive_trapezoidal(N))

# plt.figure()
# plt.title('This is the Adaptive Trapezoidal results')
# plt.plot(x,y,'*-')
# plt.xlabel(r'$log_2(N/10)$')
# plt.xlim(0,max(x))
# plt.ylabel(r'$log_{10}(Integral_Result)$')
# plt.show()
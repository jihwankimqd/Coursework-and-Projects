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


# 3) Adaptive Simpson
# Simpson's method was highly inaccurate for values of N, which were smaller than
# extremely large numbers. N had to be greater than 1e9 to approach the theoretical
# result, but it would take insanely long computational time.

def simpson(N):
    h = (b-a)/N
    Si = h*(f(a)+f(b))/3
    # only even steps
    for i in range(2,N,2):
        Si += (2*f(a+i*h))/3
    Ti = 0
    # only odd steps
    for j in range(1, N, 2):
        Ti += f(a+j*h)*(2/3)
    return h*(Si + 2*Ti)


# print(simpson(N))

# error array 
e = []
# result array
r = []
# slices array
s = []
# for plotting graph
x = []
y = []

def adaptive_simpson(N):
    sim_old = simpson(N)
    error = 1
    # To get the computer to actually compute this, the error could not be bigger than
    # 1.0e-4 anything bigger would take too long to output the result.
    accuracy = 1.0e-5
    while(error>accuracy):
        N = N*2
        sim = simpson(N)
        error = abs(sim - sim_old)/15
        sim_old = sim
        x.append(math.log(N/2,2))
        y.append(math.log(error,10))
        e.append(error)
        r.append(sim)
        s.append(N)
    # return sim
    return sim

adaptive_simpson(N)

# for i in range(0, len(e)):
#     print(i,"th Error: ", e[i],"Result: ", r[i], "Slices: ", s[i])

# # print("Adaptive Simpson Rule: ", adaptive_simpson(N))

# plt.figure()
# plt.title('This is the Adaptive Simpson results')
# plt.plot(x,y,'*-')
# plt.xlabel(r'$log_2(N_Simp/10)$')
# plt.xlim(0,max(x))
# plt.ylabel(r'$log_{10}(Integral_Result)$')
# plt.show()
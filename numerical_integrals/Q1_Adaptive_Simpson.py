import numpy as np
import matplotlib.pyplot as plt
import math
import time

def f(x):
    if x == 0:
        return(0)
    else:
        return (np.cos(x)- 2*(np.sin(x)))/(np.sqrt(x))


N = 1000000
a = 0.0
b = 1.0

# a_new to address singularities in the integral
a_new = a+ 0.000000001
N_simpson = 2


# 3) Adaptive Simpson
# Simpson's method was highly inaccurate for values of N, which were smaller than
# extremely large numbers. N had to be greater than 1e9 to approach the theoretical
# result, but it would take insanely long computational time.

def simpson(N_simpson):
    h = (b-a)/N_simpson
    Si = h*(f(a_new)+f(b))/3
    # only even steps
    for i in range(2,N_simpson,2):
        Si += (2*f(a+i*h))/3
    Ti = 0
    # only odd steps
    for j in range(1, N_simpson, 2):
        Ti += f(a+j*h)*(2/3)
    return h*(Si + 2*Ti)


# print(simpson(N_simpson))

# error array 
e = []
# result array
r = []
# slices array
s = []
# for plotting graph
x = []
y = []

def adaptive_simpson(N_simpson):
    sim_old = simpson(N_simpson)
    error = 1
    # To get the computer to actually compute this, the error could not be bigger than
    # 1.0e-4 anything bigger would take too long to output the result.
    accuracy = 1.0e-3
    while(error>accuracy):
        N_simpson = N_simpson*2
        sim = simpson(N_simpson)
        error = abs(sim - sim_old)/15
        sim_old = sim
        x.append(math.log(N_simpson/2,2))
        y.append(math.log(error,10))
        e.append(error)
        r.append(sim)
        s.append(N_simpson)
    # return sim
    return


adaptive_simpson(N_simpson)

for i in range(0, len(e)):
    print(i,"th Error: ", e[i],"Result: ", r[i], "Slices: ", s[i])

# print("Adaptive Simpson Rule: ", adaptive_simpson(N_simpson))

print("Computation Time: ", time.process_time())


plt.figure()
plt.title('This is the Adaptive Simpson results')
plt.plot(x,y,'*-')
plt.xlabel(r'$log_2(N_Simp/10)$')
plt.xlim(0,max(x))
plt.ylabel(r'$log_{10}(Integral_Result)$')
plt.show()
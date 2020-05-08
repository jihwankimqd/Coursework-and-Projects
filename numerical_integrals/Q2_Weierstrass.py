import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad
# Reusing functions
# import Adaptive_Trapezoidal_Weierstrass
# import Adaptive_Simpson_Weierstrass
# import Gaussian_Quadrature

# separate Weierstrass versions of the code had been produced to customize it into my needs
# without affecting the original code
from Q2_Adaptive_Simpson_Weierstrass import adaptive_simpson,s,e
from Q2_Adaptive_Trapezoidal_Weierstrass import adaptive_trapezoidal,slices
from Q2_Adaptive_Trapezoidal_Weierstrass import e as trap_e
from Q2_Gaussian_Quadrature_Weierstrass import gaussian
# from Adaptive_Simpson_Weierstrass import s,e
a=0.5
b=15

lower_bound = 0.0
upper_bound = 0.5

N = 10000
# addressing s outside the weierstrass function delcared it out of bound, so 
# redeclared and initialized it inside the weierstrass function
# result=0

def weierstrass(x):
    result = 0
    for i in range(0,101):
        result += (a**i)*(np.cos((b**i)*np.pi*x))
    return result

# testing output
# print(weierstrass(10))

# print(quad(weierstrass,lower_bound,upper_bound))
# true_value = 0.30755688018403043

for i in range(len(e)):
    print("Adaptive Simpson Slices: ", s[i]," Error: ", e[i])

for i in range(len(trap_e)):
    print("Adaptive Trapezoidal Slices: ", slices[i]," Error: ", trap_e[i])


print("Adaptive Simpson: ", adaptive_simpson(N))
print("Adaptive Trapezoidal: ",adaptive_trapezoidal(N))
print("Gaussian Quadrature: ", gaussian(weierstrass,lower_bound,upper_bound,N))



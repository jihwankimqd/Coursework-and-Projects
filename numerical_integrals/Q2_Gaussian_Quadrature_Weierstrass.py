import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math

a=0.0
b=0.5

a_w =0.5
b_w =15

# def weierstrass(x):
def f(x):
    result = 0
    for i in range(0,101):
        result += (a_w**i)*(np.cos((b_w**i)*np.pi*x))
    return result

# 5) Gaussian Quadrature
from gaussxw import gaussxwab

accuracy = 1e-5

n=10000
# np.seterr(divide='ignore', invalid='ignore')
# ignores overflow error for np.cos which occurs for large values of n. n greater than
# 9000 seems to cause overflow error, but will still output accurate result.
# it seems to be a datatype limitation of the numpy library
np.seterr(all='ignore')



#compare error with simpson and trapezoidal

def gaussian(f, a, b, n=n):
    x, w = gaussxwab(n, a, b)

    # while(error > accuracy):
    #     n = n*2
    #     x, w = gaussxwab(n, a, b)
    #     print(n)
    #     print(error)
    return sum(f(x) * w)
# print("Gaussian Quadrature Method: ", gaussian(f,a,b))

# gaussian(f,a,b)
# print(quad(f,a,b))

# # error array 
# e = []
# # result array
# r = []
# # slices array
# slices = []
# # for plotting graph
# x = []
# y = []

# print(gaussian(f,a,b,n))

# # Gaussian funciton will not work well,
# # The function is too sharp/fluctuating and poorly behaving integral
# def gaussian_error(n):
#     error = abs(0.30755688018403043-gaussian(f,a,b))
#     print(error)
#     while(error > accuracy):
#         n = n*2
#         # print(n)
#         # print(gaussian(f,a,b,n))
#         error = abs(0.30755688018403043-gaussian(f,a,b,n))
#         print(error)
#         x.append(math.log(n/2,2))
#         y.append(math.log(error,10))
#         e.append(error)
#         slices.append(n)
#         r.append(gaussian(f,a,b,n))
#     return gaussian(f,a,b,n)

# print(gaussian_error(n))

# for i in range(len(e)):
#     print("Gaussian Quadrature: ", r[i], "Error: ", e[i], "Slices: ", slices[i])


# print("Comparison with the Scipy Quad Function")
# print("Scipy Integration: ", quad(f,a,b), "Gaussian Quadrature: ", gaussian(f,a,b), "Error: ", error, "Slices: ", n)


# plt.figure()
# plt.title('This is the Gaussian Quadrature results')
# plt.plot(x,y,'*-')
# plt.xlabel(r'$log_2(n/10)$')
# plt.xlim(0,max(x))
# plt.ylabel(r'$log_{10}(Integral_Result)$')
# plt.show()
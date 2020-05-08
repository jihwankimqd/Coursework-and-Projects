import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math
import time

def f(x):
    if x == 0:
        return(0)
    else:
        return (np.cos(x)- 2*(np.sin(x)))/(np.sqrt(x))


N = 10
a = 0.0
b = 1.0

# a_new to address singularities in the integral
a_new = a+ 0.000000001
accuracy = 1e-3

# code to visually see if the f(x) is actually correctly input as intended. 
# x = np.arange(0,10,0.1) 
# y = f(x)
# fig = plt.figure()
# plt.plot(x,y)
# plt.show()

# print(quad(f,a,b))
true_value = 0.5679752689070126

# # 1)
# # Left Rectangle Rule
# def leftrec(N):
#     h = (b-a_new)/N
#     s = 0
#     for i in range(1, N):
#         s += f(a_new+(i-1)*h)
#     return h*s

# error_left = abs(leftrec(N) - true_value)

# # error array 
# e = []
# # result array
# r = []
# # slices array
# slices = []

# while(error_left > accuracy):
#     N = N*10
#     print(N)
#     error_left = abs(leftrec(N) - true_value)
#     print(error_left)
#     e.append(error_left)
#     slices.append(N)
#     r.append(leftrec(N))

# for i in range(len(e)):
# # print("Left Rectangle Rule: ", leftrec(N), "Error: ", leftrec(N)-true_value)
#     print("Left Rectangle Rule: ", r[i], "Error: ", e[i], "Slices: ", slices[i])
    

# # Tried the left rectangle rule, but of course there will be an error, because 
# # at the first iteration, the computer will try to divide by zero. Therefore,
# # I should try the mid rectangle rule.
# edit. After adjusting the boundaries by a small value, it seems to be working.

# Mid Rectangle Rule
def midpointrec(N):
    h = (b-a)/N
    s = 0
    for i in range(0, N-1):
        s += f(a+(h/2)+(i*h))
    return h*s

error_mid = abs(midpointrec(N) - true_value)


# error array 
e = []
# result array
r = []
# slices array
slices = []
# for plotting graph
x = []
y = []



while(error_mid > accuracy):
    N = N*2
    # print(N)
    error_mid = abs(midpointrec(N) - true_value)
    # print(error_mid)
    x.append(math.log(N/2,2))
    y.append(math.log(error_mid,10))
    e.append(error_mid)
    slices.append(N)
    r.append(midpointrec(N))

# print("Midpoint Rectangle Rule: ", midpointrec(N), "Error: ", midpointrec(N)-true_value)
for i in range(len(e)):
    print("Midpoint Rectangle Rule: ", r[i], "Error: ", e[i], "Slices: ",slices[i])

print("Computation Time: ", time.process_time())


# Takes forever to calculte error accurate to 1e-4 it is certainly much larger than other methods

plt.figure()
plt.title('This is the Midpoint Rectangle results')
plt.plot(x,y,'*-')
plt.xlabel(r'$log_2(N/10)$')
plt.xlim(0,max(x))
plt.ylabel(r'$log_{10}(Integral_Result)$')
plt.show()
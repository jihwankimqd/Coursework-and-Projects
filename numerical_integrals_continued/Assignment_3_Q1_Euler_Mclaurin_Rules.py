import numpy as np
import matplotlib.pyplot as plt
import math
import time

def f(x):
    if x == 0:
        return(0)
    else:
        return ((x**4)-(2*x)+1)


N = 2
a = 0.0
b = 2.0

def central_difference(x,N):
    # h = (b-a)/N
    h = 1e-5
    derivative = (f(x+(h/2)) - f(x-(h/2)))/h
    return derivative

def trapezoidal_part(N):
    h = (b-a)/N
    s = 0.5*f(a) + 0.5*f(b)
    for i in range(1,N):
        s = s + f(a+(i*h))
    s = s*h
    return s

def derivative_part(N):
    h = (b-a)/N
    s = central_difference(a,N)-central_difference(b,N)
    total = (1/12)*(h**2)*s
    return total
    
def euler_maclaurin(N):
    integral = trapezoidal_part(N) + derivative_part(N)
    return integral

# error array 
e = []
# result array
r = []
# slices array
slices = []
# for plotting graph
x = []
y = []

def error_adjust(N):
    s_old = euler_maclaurin(N)
    error = 1
    # To get the computer to actually compute this, the error could not be bigger than
    # 1.0e-4 anything bigger would take too long to output the result.
    accuracy = 1e-5
    while(error>accuracy):
        N = N*2
        s = euler_maclaurin(N)
        error = abs(s - s_old)/15
        s_old = s
        x.append(math.log(N/2,2))
        y.append(math.log(error,10))
        e.append(error)
        r.append(s)
        slices.append(N)
    # return sim
    return

error_adjust(N)

for i in range(0, len(e)):
    print(i,"th Error: ", e[i],"Result: ", r[i], "Slices: ", slices[i])

print("Computation Time: ", time.process_time())


plt.figure()
plt.title('This is the Euler Maclaurin Rules results')
plt.plot(x,y,'*-')
plt.xlabel(r'$log_2(N/10)$')
plt.xlim(0,max(x))
plt.ylabel(r'$log_{10}(Integral_Result)$')
plt.show()
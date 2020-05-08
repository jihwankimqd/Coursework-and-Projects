import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math
import time

# Computation time takes too long to acheive accuracy of 1e-4. 

def f(x):
    if x == 0:
        return(0)
    else:
        return (np.cos(x)- 2*(np.sin(x)))/(np.sqrt(x))


N = 5
a = 0.0
b = 1.0

# a_new to address singularities in the integral
a_new = a+ 0.000000001

true_value = 0.5679752689070126


# 4) Romberg

# Helper function trap to accompany the Romberg method
def Trap(f, a=0, b=0, n=1):
    h = (b-a)/n
    I = h*1/2*(f(a)+f(b))
    for i in range(1,n):
        I += h*f(a+i*h)
    return(I)

# Tried setting the a value to 0.00000001, but it gives slightly more inaccurate
# result compared to just setting f(x)=0 when x = 0.
# Therefore, edited the f(x) above to adjust for this.


def Romberg(N):
    Romb = np.zeros((N,N))
    Romb[0,0] = Trap(f,a,b,2)
    for i in range(1,N):
        Romb[i,0] = Trap(f,a,b,2*2**i)
    for i in range(1,N):
        for j in range(1,i+1):
            Romb[i,j] = Romb[i,j-1] + (Romb[i,j-1] - Romb[i-1,j-1])/(4**j -1)
    return (Romb)

# error array 
e = []
# result array
r = []
# slices array
slices = []
# for plotting graph
x = []
y = []

error = abs(Romberg(N)[N-1][N-1]-true_value)
accuracy = 1e-2
count = 1

while(error > accuracy and count <= 20):
    N = N+1
    count += 1
    # print(N)
    error = abs(Romberg(N)[N-1][N-1]-true_value)
    # print(error)
    x.append(math.log(N/2,2))
    y.append(math.log(error,10))
    e.append(error)
    slices.append(N)
    r.append(Romberg(N)[N-1][N-1])



# printing the last element of the romberg 2D array, which is the most accurate
# calculated value.
# print("Romberg Method: ",Romberg(N)[N-1][N-1], "Error: ", Romberg(N)[N-1][N-1]-0.5679752689070126)

for i in range(0,len(e)):
    print("Romberg Method: ",r[i], "Error: ", e[i], "Slices: ", slices[i])



# print(quad(f,a,b))
print("Computation Time: ", time.process_time())


plt.figure()
plt.title('This is the Romberg results')
plt.plot(x,y,'*-')
plt.xlabel(r'$log_2(N/10)$')
plt.xlim(0,max(x))
plt.ylabel(r'$log_{10}(Integral_Result)$')
plt.show()
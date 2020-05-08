import numpy as np
import matplotlib.pyplot as plt

G = 6.674*(10**(-11))
M = 5.974*(10**(24))
m = 7.348*(10**(22))
R = 3.844*(10**(8))
w = 2.662*(10**(-6))

def f(r):
    y = ((G*M)/(r**2)) - ((G*m)/((R-r)**2)) - ((w**2)*r)
    return y
def df(r):
    dy = ((-2*G*M)/(r**3))-((2*G*m)/((R-r)**3)) -(w**2)
    return dy

# def f(r):
#     y =  ((w**2)*r)
#     return y
# def df(r):
#     dy = (w**2)
#     return dy

accuracy = 1*(10**-5)
r0 = 750000
All_r=[]
All_r.append(r0)
# x_array = [0]

# for i in range(1,10000):
#     # x_array.append(i)
#     r1 = f(i)
#     All_r.append(r1)

# plt.figure()
# plt.plot(x_array,All_r)
# plt.show()

Have_Solution = False

# Newton's Method
for i in range(100):
    r1=r0-f(r0)/df(r0)
    if abs(r1-r0)<accuracy:
        Have_Solution=True
        print('Repetition: ',i)
        break
    else:
        r0=r1
    All_r.append(r0)

print(All_r)

if Have_Solution:
    plt.figure()
    plt.plot(All_r,'o-')
    plt.xlabel("# of interation")
    plt.ylabel("Solution")
    plt.show()
    print("Solution: ",All_r[-1])
else:
    print("No Solution")
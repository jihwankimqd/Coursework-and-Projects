import numpy as np
import matplotlib.pyplot as plt

# Value of c
c = 2

# Function 
def f(x):
    y = 1-np.exp(-c*x)+(0.2*x)
    return y

# def overrelaxation():
#     accuracy = 10**(-6)
#     Max_Interation=10000
#     x0=1
#     All_x=[]
#     All_x.append(x0)
#     Have_Solution = False
#     w=0.5

#     for i in range(Max_Interation):
#         x1= (1 + w) * f(All_x[-1]) - w * All_x[-1]
#         if abs(x0-x1)<accuracy:
#             Have_Solution = True
#             print('Iteration: ', i+1)
#             break
#         else:
#             x0=x1
#         All_x.append(x0)
#     return x0

# overrelaxation()

def overrelax():
    accuracy = 10**(-6)
    init = 1
    x = [init]

    # tested with different values of w, but -1 gave the smallest number = 2
    # w = 0.3, iteration = 10
    # w = 0.4, iteration = 8
    # w = 0.5, iteration = 7
    # w = 0.6, iteration = 6
    # w = 0.7, iteration = 4
    # w = 0.8, iteration = 5
    # w = 0.9, iteration = 7

    # at w = -1, iteration = 2 only. But the solution is wrong. 
    # any value more negative than -1 gives unstable and incorrect results.

    w = (0.8)
    x_ = (1 + w) * f(x[-1]) - w * x[-1]
    x.append(x_)
    if abs(x[-1] - x[-2]) == 0:
        e = 0
    elif ((f(x[-1]) - f(x[-2])) / (x[-1] - x[-2])) == 1:
        e = abs(x[-1] - x[-2])
    else:
         f_ = (f(x[-1]) - f(x[-2])) / (x[-1] - x[-2])
         e = (x[-1] - x[-2]) / (1 - 1/((1 + w) * f_ - w))

    while abs(e) > accuracy:
        x_ = (1 + w) * f(x[-1]) - w * x[-1]
        x.append(x_)
        if abs(x[-1] - x[-2]) == 0:
            e = 0
        else:
            f_ = (f(x[-1]) - f(x[-2])) / (x[-1] - x[-2])
            e = (x[-1] - x[-2]) / (1 - 1 / ((1 + w) * f_ - w))

    return x

fig = plt.figure()
x_over = overrelax()
print('Solution: ', x_over[-1])
print('Number of Iteration: ', (len(x_over)))
fig.suptitle('Solution Plot Using Over-Relaxation Method w=0.8')
plt.plot(x_over,'o-')
plt.xlabel("Number of interation")
plt.ylabel("Solution")
plt.show()
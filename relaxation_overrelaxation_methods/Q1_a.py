import numpy as np
import matplotlib.pyplot as plt

# Value of c
c = 3

# Function 
def f(x):
    y = 1-np.exp(-c*x)+(0.2*x)
    return y

# Plot the graph
fig = plt.figure()
fig.suptitle('Initial Plot')
x = np.linspace(0,5,100)
plt.plot(x,x,'r*',label = 'Plot for x=x')
plt.plot(x,f(x),'b*',label = 'Plot for x=f(x)')
plt.legend()
plt.show()  




def relaxation():
    accuracy=10**(-6)
    Max_Interation=10000
    x0=1
    All_x=[]
    All_x.append(x0)
    Have_Solution = False

    for i in range(Max_Interation):
        x1=f(x0)
        if abs(x0-x1)<accuracy:
            Have_Solution = True
            # i+1 because i starts at 0. Just a matter of definition of the iteration.
            print('Iteration: ', i+1)
            break
        else:
            x0=x1
        All_x.append(x0)
    
    if Have_Solution:
        fig2 = plt.figure()
        fig2.suptitle('Solution Plot Using Relaxation Method')
        plt.plot(All_x,'o-')
        plt.xlabel("Number of interation")
        plt.ylabel("Solution")
        plt.show()
    else:
        print("We did not find a solution!")
    
    return All_x[-1]

print('Solution: ',relaxation())
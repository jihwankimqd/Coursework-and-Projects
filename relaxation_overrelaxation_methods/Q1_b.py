import numpy as np
import matplotlib.pyplot as plt

# Value of c

c_list = np.arange(0,4,0.02)

# Function 
def f(x,c):
    y = 1-np.exp(-c*x)+(0.2*x)
    return y

# Plot the graph
# fig = plt.figure()
# fig.suptitle('Initial Plot')
# x = np.linspace(0,5,100)
# plt.plot(x,x,'r*',label = 'Plot for x=x')
# plt.plot(x,f(x),'b*',label = 'Plot for x=f(x)')
# plt.legend()
# plt.show()  

def relaxation(c):
    accuracy=10**(-6)
    Max_Interation=10000
    x0=1
    All_x=[]
    All_x.append(x0)
    Have_Solution = False

    for i in range(Max_Interation):
        x1=f(x0,c)
        if abs(x0-x1)<accuracy:
            Have_Solution = True
            break
        else:
            x0=x1
        All_x.append(x0)

    return x0
    # if Have_Solution:
    #     fig2 = plt.figure()
    #     fig2.suptitle('Solution Plot Using Relaxation Method')
    #     plt.plot(All_x,'o-')
    #     plt.xlabel("Number of interation")
    #     plt.ylabel("Solution")
    #     plt.show()
    # else:
    #     print("We did not find a solution!")
    
# relaxation()

x = []
for i in range(len(c_list)):
    x.append(relaxation(c_list[i]))

plt.figure()
plt.plot(c_list,x,'b*')
plt.xlabel("Value of c")
plt.ylabel("Solution")
plt.show()

print('Solution: ', x[-1])
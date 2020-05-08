import numpy as np
import matplotlib.pyplot as plt

#initial setup
alpha = 1
beta = 0.5
gamma = 0.5
delta = 2

x_initial = 2
y_initial = 2

t_start = 0.0
t_final = 30.0
N = 20000
h = (t_final-t_start)/N
tpoints = np.arange(t_start,t_final,h)

def f_x(x,y):
    return (alpha*x) - (beta*x*y)

def f_y(x,y):
    return (gamma*x*y) - (delta*y)

def f(r,t):
    x = r[0]
    y = r[1]
    # return [f_x(x,y),f_y(x,y)]
    return np.array([f_x(x,y),f_y(x,y)],float)


xpoints = []
ypoints = []
# r = [x_initial,y_initial]
r = np.array([x_initial,y_initial],float)

for t in tpoints:
    xpoints.append(r[0])
    ypoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t)
    k3 = h*f(r+0.5*k2,t)
    k4 = h*f(r+k3,t)
    r += (k1+2*k2+2*k3+k4)

plt.figure()
plt.plot(tpoints,xpoints, label = "x(t)_Rabbits")
plt.plot(tpoints,ypoints, label = "y(t)_Foxes")
plt.xlabel("T")
plt.ylabel("x(t)_Rabbits,y(t)_Foxes")
plt.legend()
plt.show()


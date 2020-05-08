import numpy as np
import matplotlib.pyplot as plt


# RC = 0.01 #0.1 #1

def V_in(t):
    # if even
    if np.floor(2*t) % 2 == 0:
        return 1
    #if odd
    if np.floor(2*t) % 2 == 1:
        return (-1)

V_out = 0

def f(V,t,RC):
    return 1/RC *(V_in(t) - V)


t_start = 0.0
t_final = 10.0
N = 5000
h = (t_final-t_start)/N
tpoints = np.arange(t_start,t_final,h)

def vary_RC(RC):
    Vpoints = []
    #initial V = V_out = 0
    V = V_out
    for t in tpoints:
        Vpoints.append(V)
        k1 = h*f(V,t, RC)
        k2 = h*f(V+0.5*k1,t+0.5*h,RC)
        k3 = h*f(V+0.5*k2,t+0.5*h,RC)
        k4 = h*f(V+k3,t+h,RC)
        V += (k1+2*k2+2*k3+k4)/6
    return Vpoints

plt.figure()
plt.plot(tpoints,vary_RC(0.01),label="0.01")
plt.plot(tpoints,vary_RC(0.1),label="0.1")
plt.plot(tpoints,vary_RC(1),label="1")
plt.xlabel("t")
plt.ylabel("V(t)")
plt.legend()
plt.show()


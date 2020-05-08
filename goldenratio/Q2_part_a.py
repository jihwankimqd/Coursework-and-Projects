import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def bulb(x):
    y = x**3/(np.exp(x)-1)
    return y

accuracy = 1
z = (1 + np.sqrt(5))/2
hc = 1.23984193*(10**3)  
lambda_1 = 390
lambda_2 = 750
kB = 8.6173303*(10**-5)
upper_const = hc / (lambda_1 * kB)
lower_const = hc / (lambda_2 * kB)

ans,error = integrate.quad(bulb,lower_const,upper_const)
result = []
T_list = np.linspace(300,10000)

for Temperature in T_list:
    upper = upper_const/Temperature
    lower = lower_const/Temperature
    ans, error = integrate.quad(bulb, lower, upper)
    result.append(ans)

for i in range(len(result)):
    result[i] = result[i]*15/(np.pi**4)

plt.figure()
plt.plot(T_list,result)
plt.xlabel('Temperature')
plt.ylabel('Result')
plt.show()
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

def integral(temp):
    upper = upper_const/temp
    lower = lower_const/temp
    ans= integrate.quad(bulb, lower, upper)[0]
    return ans
# plt.figure()
# plt.plot(T_list,result)
# plt.xlabel('Temperature')
# plt.ylabel('Result')
# plt.show()

# Max efficiency around 7000K from part_a. Therefore choose T1 and T4 to fit 7000K in between.
T1 = 6000
T4 = 8000
T2 = T4-(T4-T1)/z
T3 = T4+(T4-T1)/z

# Initial values of eta
initial_T1 = integral(T1)
initial_T2 = integral(T2)
initial_T3 = integral(T3)
initial_T4 = integral(T4)

# golden ratio search loop
while T4 - T1 > accuracy:
    if initial_T2 < initial_T3 :
        T4, initial_T4 = T3, initial_T3
        T3, initial_T3 = T2, initial_T2
        T2 = T4 - (T4 - T1)/z
        initial_T2 = integral(T2)
    else:
        T1, initial_T1 = T2, initial_T2
        T2, initial_T2 = T3, initial_T3
        T3 = T1 + (T4 - T1)/z
        initial_T3 = integral(T3)

print('The temperature of max efficiency is', 0.5 * (T1 + T4))


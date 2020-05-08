import numpy as np
import matplotlib.pyplot as plt
import math
from random import random

# equation of sphere which can be deduced from the question
def sphere(x,y,z):
    return ((x**2)+(y**2)+(z**2))

# equation of cylinder which can be deduced from the question
def cylinder(x,y):
    return (((x-0.5)**2)+(y**2))

# helper function to check if random point is within the sphere
def in_sphere(k):
    if k < 1:
        return 1
    else:
        return 0
    
# helper function to check if random point is within the cylinder
def in_cylinder(k):
    if k < 0.25:
        return 1
    else:
        return 0

# N is the sampling number, count is used for counting
N = 100000
count = 0

for i in range(N):
    x = random()
    # y = -0.5*random()+0.5*random()
    # z = -random()+random()

    y= 0.5*random()
    z= random()

    # if (in_sphere(sphere(x,y,z)) and in_cylinder(cylinder(x,y))):
    # if point lies within the sphere and the cylinder, add 1 to counter
    if (in_sphere(sphere(x,y,z)) and in_cylinder(cylinder(x,y))):

        count+=1

    # if(sphere(x,y,z)<1):
    #     count+=1


print('Count: ',count)
monte_carlo_result = 2*count/N
# Monte Carlo Result
print('Monte Carlo Result: ', monte_carlo_result)

# Compare with analytical result that can be easily calculated using multivariable calculus
analytic_result = ((2/9)*((3*np.pi)-4))
print('Analytic Result: ',analytic_result)

error = monte_carlo_result-analytic_result
print('Error: ', error)
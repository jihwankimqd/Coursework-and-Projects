import numpy as np
import math

a = np.array([[3,-1,-1], [-1,4,-1], [-1,-1,3]])
b = np.array([5,5,0])
x = np.linalg.solve(a,b)

print (x)
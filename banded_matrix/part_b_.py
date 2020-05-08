import numpy as np
import math

# a = np.array([[3,-1,-1], [-1,4,-1], [-1,-1,3]])
# b = np.array([5,5,0])
# x = np.linalg.solve(a,b)
# print (x)

# create Av = w matrix
V_in = 5
N = 6
A = np.zeros(shape=(N,N))
B = np.zeros(N)
B[0] = V_in
B[1] = V_in

for i in range(N):
    if(i == 0):
        A[i][0] = 3
        A[i][1] = -1
        A[i][2] = -1
    
    if(i == 1):
        A[i][0] = -1
        A[i][1] = 4
        A[i][2] = -1
        if(N > 3):
            A[i][3] = -1
    
    if(i >= 2 and i<(N-2)):
        A[i][i-2] = -1
        A[i][i-1] = -1
        A[i][i] = 4
        A[i][i+1] = -1
        A[i][i+2] = -1
    
    if(i == N-2):
        A[i][N-1-3] = -1
        A[i][N-1-2] = -1
        A[i][N-1-1] = 4
        A[i][N-1] = -1

    if(i == N-1):
        A[i][N-1-2] = -1
        A[i][N-1-1] = -1
        A[i][N-1] = 3

print("Matrix A")
print(A)

print("Matrix B")
print(B)





        

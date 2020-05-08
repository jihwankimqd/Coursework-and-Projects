import numpy as np
import math
import time
from banded_ import banded


# a = np.array([[3,-1,-1], [-1,4,-1], [-1,-1,3]])
# b = np.array([5,5,0])
# x = np.linalg.solve(a,b)
# print (x)

# create Av = w matrix
V_in = 5
N = 10000
A = np.zeros(shape=(N,N))
B = np.zeros(N)
B[0] = V_in
B[1] = V_in

def initialize():  
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

# np.linalg.solve Method
initialize()

# print("Matrix A")
# print(A)
# print("Matrix B")
# print(B)

# V = np.linalg.solve(A,B)
# print("Print np.linalg.solve Method Matrix V")
# print(V)
# print("Computation Time: ", time.process_time())



# Baned Method Below

# Create a matrix which is suitable for usage in banded function
# rearranges the original array like shown in page 4 of lecture slides 14
def bandify(up,down):
    M = np.zeros(shape=(up+down+1,N))
    
    for i in range(N):
        for j in range(N):
            if(A[i][j] != -1 and A[i][j] != 0):
                M[up][j] = A[i][j]
                # below the diagonal line
                if(down+1 < N and i+1 < N):
                    M[down+1][j] = A[i+1][j]
                if(down+2 < N and i+2 < N):
                    M[down+2][j] = A[i+2][j]
                # above the diagonal line
                if(up-1 < N and i-1 < N):
                    M[up-1][j] = A[i-1][j]
                if(up-2 < N and i-2 < N):
                    M[up-2][j] = A[i-2][j]

    return M

print('Bandify')
M = (bandify(2,2))
print(M)
print("Computation Time: ", time.process_time())

# M = (bandify(2,2))


# initialize()

# print("Matrix A")
# print(A)
# print("Matrix B")
# print(B)

x = banded(M,B,2,2)
print(" ")
print("Print banded Method Matrix V")
print(x)
print("Computation Time: ", time.process_time())

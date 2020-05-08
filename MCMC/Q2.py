#Monte Carlo simulations for 2D Ising model with grid N*N

import numpy as np
from pylab import plot,figure,errorbar,hist,subplot,title,xlabel,ylabel,legend
import time as time
import numpy as np
import matplotlib.pyplot as plt

# start time of calculation

#Hamiltonian
J=3
Latt_N = 10
Latt_M = 10
low_T=1
high_T=20
delta_T=0.2

#Monte Carlo setup
Nbins = 100
Nsweep = 10

# Size of lattice
N = 10

# n1, n2  = 1.0/(Nbins*N*N), 1.0/(Nbins*Nbins*N*N)
n1, n2  = 1.0/(Nbins*Nsweep), 1.0/((Nbins*Nsweep)**2)



#prepare the initial state
latt=np.zeros([Latt_M,Latt_N])
for nx in range(Latt_M):
    for ny in range(Latt_N):
        latt[nx,ny]=np.sign(np.random.random()-0.5)

#get the energy difference after flipping the spin at (nx,ny)
def get_delta_E(nx,ny):
    nx1=np.mod(nx-1,Latt_M)
    nx2=np.mod(nx+1,Latt_M)
    ny1=np.mod(ny-1,Latt_N)
    ny2=np.mod(ny+1,Latt_N)
    delta_E=2*J*latt[nx,ny]*(latt[nx1,ny]+latt[nx2,ny]+latt[nx,ny1]+latt[nx,ny2])
    return delta_E

#calculate the auto-correlation
def auto_corr(data):
    data_tmp=np.array(data)
    N=data_tmp.size
    Num_auto=int(0.1*N)
    
    if Num_auto>500:
        Num_auto=500
    
    data_tmp=data_tmp-sum(data_tmp)/N
    
    auto_corr = np.zeros(Num_auto)
    for ni in range(Num_auto):
        auto_corr[ni]=sum((data_tmp[0:N-ni])*(data_tmp[ni:N]))

    return auto_corr/auto_corr[0]

# Magnetism
num_T=np.arange(low_T,high_T,delta_T).size
all_M=np.zeros([num_T,Nbins*Nsweep])
all_M_abs=np.zeros([num_T,Nbins*Nsweep])
aver_M=np.zeros(num_T)
aver_M_abs=np.zeros(num_T)
# Energy
all_E=np.zeros([num_T,Nbins*Nsweep])
aver_E=np.zeros(num_T)
# Heat Capacity
capacity=np.zeros([num_T,Nbins*Nsweep])
avg_capacity=np.zeros(num_T)
# Susceptibility
sus=np.zeros([num_T,Nbins*Nsweep])
avg_sus=np.zeros(num_T)

nT=0


#calcuating the nearest neighbours
# def find_neighbors(latt, x, y):
#     left   = (x, y - 1)
#     right  = (x, (y + 1) % 10)
#     top    = (x - 1, y)
#     bottom = ((x + 1) % 10, y)

#     return [latt[left[0], left[1]],
#             latt[right[0], right[1]],
#             latt[top[0], top[1]],
#             latt[bottom[0], bottom[1]]]
#calculating the energy of the configuration
# def energy(latt, x ,y):
#     return (-J) * latt[x, y] * sum(find_neighbors(latt, x, y))

# size of lattice
# def calcEnergy(latt):
#     '''Energy of a given configuration'''
#     energy = 0
#     for i in range((Latt_M)):
#         for j in range((Latt_N)):
#             S = latt[i,j]
#             nb = latt[(i+1)%N, j] + latt[i,(j+1)%N] + latt[(i-1)%N, j] + latt[i,(j-1)%N]
#             energy += -nb*S
#     return energy/4.
def calcEnergy(latt,i,j):
    '''Energy of a given configuration'''
    energy = 0
    S = latt[i,j]
    nb = latt[(i+1)%N, j] + latt[i,(j+1)%N] + latt[(i-1)%N, j] + latt[i,(j-1)%N]
    energy += -nb*S
    return energy/4.


for T in np.arange(low_T,high_T,delta_T):
    nt2=0
    E1=E2=M1=M2=0
    start_time = time.time()
    for nb in range(Nbins):        
        for ns in range(Nsweep):
            for nl in range(Latt_N*Latt_M):
                nx=np.random.randint(Latt_M)
                ny=np.random.randint(Latt_N)
                delta_E=get_delta_E(nx,ny)
                if np.exp(-delta_E/T)>np.random.random():
                    latt[nx,ny] = - latt[nx,ny]
         
            # Magnetization
            all_M[nT,nt2]=sum(sum(latt))/Latt_M/Latt_N
            all_M_abs[nT,nt2]=abs(all_M[nT,nt2])


            # Energy
            all_E[nT,nt2] = (calcEnergy(latt,nx,ny))

            # Capacity
            E1 += all_E[nT,nt2]
            E2 += all_E[nT,nt2]*all_E[nT,nt2]
         
            # Susceptibility
            M1 += all_M[nT,nt2]
            M2 += all_M[nT,nt2]*all_M[nT,nt2]

            nt2 +=1
    # Magnetization        
    aver_M[nT]=sum(all_M[nT,:])/Nbins/Nsweep
    aver_M_abs[nT]=sum(all_M_abs[nT,:])/Nbins/Nsweep

    # Energy
    aver_E[nT] = sum(all_E[nT,:])/Nbins/Nsweep


    # Specific Heat Capacity
        # capacity_1 = capacity-E2
        # avg_capacity[nT] = sum(capacity_1[nT,:])/Nbins/Nsweep
    # capacity = np.var(all_E)/(T**2)

    avg_capacity[nT]   = (n1*E2 - n2*M1*M1)/(T**2)

    # Susceptibility 

    avg_sus[nT] = (n1*M2 - n2*E1*E1)/(T)

    nT+=1
    print("Simulation at temperature T= ", T)


figure(figsize=(18, 10))

subplot(221)
title('Energy vs temperature')
plot(np.arange(low_T,high_T,delta_T),aver_E,'bo')
xlabel('Temperature')
ylabel('Energy')

subplot(222)
title('Absolute Magnetization vs temperature')
plot(np.arange(low_T,high_T,delta_T),aver_M_abs,'bo')
xlabel('Temperature')
ylabel('Absolute Magnetization')

subplot(223)
title('Capacity vs temperature')
plot(np.arange(low_T,high_T,delta_T),avg_capacity,'bo')
xlabel('Temperature')
ylabel('Capacity')

subplot(224)
title('Susceptibility vs temperature')
plot(np.arange(low_T,high_T,delta_T),avg_sus,'bo')
xlabel('Temperature')
ylabel('Susceptibility')

plt.show()
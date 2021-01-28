#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:46:43 2020

@author: Lassi
"""

"""RANDOM WALKERS IN 1D"""

import numpy as np
import matplotlib.pyplot as plt

"""Construct an emptry matrix with dimensions of (Iterations, M) where M is 
the length of the lattice in 1D. The first row will be initialized with random 
occupation of walkers. The walkers are then moved individually in random 
directions and the next row in the matrix is updated according to the movement.
The third row removes the double occupancy according to A + A -> 0 and moves 
the walkers again. This is looped over some number of iterations itr. 
    The number of walkers at every iteration is given by the number of ones in 
each row.
"""

itr = 100
M = 500 #Do 500 for the eventplot and Do 10000 for the other plots

#### For 1D
a1d = np.zeros(shape=(itr,M),dtype=int)
# Init a random occupation in 2D lattice for the first iteration 
a1d[0] = np.random.choice([0,1],size=(M), p=[0.5, 0.5])

# Reducing the probability of occupancy: 
# p=[0.2, 0.8], p=[0.5, 0.5], p=[0.8, 0.2]
# where p=[x,y] x % zeroes and y % ones

for i in range(itr-1): #Have to put -1 otherwise we go out of bounds 
    for x in range(M):
        if a1d[i][x] == 1: #This kills the double occupancy automatically
            #print(x)
            mov = np.random.randint(2) #0 is left and 1 is right movement
            #Test that the directions work correctly before going random
            #mov = 0
            #mov = 1
            if mov == 0 and x != 0:
                a1d[i+1][x-1] += 1
            elif mov == 1 and x != (M-1):
                a1d[i+1][x+1] += 1
            #If x != 0 or x != (M-1) is not satisfied
            #we are at the border and we dont move.
            else: 
                a1d[i+1][x] += 1
print('a1d = \n', a1d)


# Read and append the number of ones in every row to plot no. walkers 
# vs no. iterations

no_arr = np.zeros(shape=(1,itr), dtype=int)
for ii in range(itr):
    for xx in range(M):
        if a1d[ii][xx] == 1:
            no_arr[0][ii] += 1 # Array of number of walkers at every iteration
           #print(xx)


"""Plotting"""
x = np.linspace(1,itr,itr)
t = np.linspace(1, itr, 100, dtype=float) #have to start from t >= 1?

# #Plot the __number__ of walkers as a function of time
# plt.title('Number of Viscous Walkers in 1D')
# plt.xlabel('Time (arb. units)')
# plt.ylabel('Number of Walkers')
# plt.plot(x, no_arr.T, label='Stochastic model')

# """Analytical in 1D: rho(t) ~ t**(-1/2)"""
# plt.plot(t, no_arr[0][0]*t**(-1/2),label='Analytical model \n'
#           r'$\rho(t) = \rho_0 t^{-1}$')
# plt.legend()
# plt.show()

#Plot the __density__ as a function of time (1 time unit = 1 iteration)
V = M

plt.title('Density of Viscous Walkers in 1D')
plt.xlabel('Time (Arb. units)')
plt.ylabel('Density of walkers (1/M)')
plt.plot(x, no_arr.T/V, label='Stochastic model')

"""Analytical in 1D: rho(t) ~ t**(-1/2)"""
#t = np.linspace(1, itr, 100, dtype=float) #have to start from t >= 1?
plt.plot(t, no_arr[0][0]/V*t**(-1/2),label='Analytical model \n'
          r'$\rho(t) = \rho_0 t^{-1/2}$')
plt.legend()
plt.show()

#Log-Log plot of the density
plt.title('log-log plot of the density of Walkers in 1D')
plt.xlabel('Time (arb. units)')
plt.ylabel('Density of walkers (1/M)')
plt.loglog(x, no_arr.T/V, label='Model')
plt.loglog(t, no_arr[0][0]/V*t**(-1/2), label='Analytical model \n'
          r'$\rho(t) = \rho_0 t^{-1/2}$')
plt.legend()
plt.show()

# """Plot 1D Walkers"""

# ## Getting positions of walkers on the x-axis at different iterations steps
# pos_init = []
# for xxx in range(M):
#     if a1d[0][xxx] == 1:
#         pos_init.append(xxx) 

# pos_2 = []
# for xxx in range(M):
#     if a1d[1][xxx] == 1:
#         pos_2.append(xxx)

# pos_10 = []
# for xxx in range(M):
#     if a1d[9][xxx] == 1:
#         pos_10.append(xxx)

# pos_49 = []
# for xxx in range(M):
#     if a1d[49][xxx] == 1:
#         pos_49.append(xxx)

# pos_final = []
# for xxx in range(M):
#     if a1d[itr-1][xxx] == 1:
#         pos_final.append(xxx) 

        
# colors1 = np.array([0,0,0])
# data_1 = np.array(pos_init)
# data_2 = np.array(pos_2)
# data_10 = np.array(pos_10)
# data_99 = np.array(pos_49)
# data_100 = np.array(pos_final)

# plt.title('1D Evolution of Walkers with initial Walkers = '  
#           +str(no_arr[0][0]))
# plt.xlabel('Position')
# plt.yticks(np.arange(6), ('Itr=0', 'Itr=1','Itr=2', 'Itr=10', 
#                           'Itr=50', 'Itr=100'))
# plt.xticks(np.arange(0, M+1, step = 100)) #Do step of M/10
# plt.hlines([1,2,3,4,5], 0, M, colors='b')

# lineoffsets1 = np.array([1, 2, 3, 4, 5])
# linelengths1 = [0.5, 0.5, 0.5, 0.5, 0.5]
# plt.eventplot([data_1, data_2, data_10, data_99, data_100], colors=colors1, 
#               lineoffsets=lineoffsets1, linelengths=linelengths1)





#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 03:32:17 2020

@author: Lassi
"""

"""RANDOM WALKERS IN 3D"""

import numpy as np
import matplotlib.pyplot as plt

"""  The 1D code is easily extended to HIGHER DIMENSIONS by increasing the 
dimensions of the initial matrix and the number of random directions for the 
movement.
    The first index of the matrix is always the no. of iteration."""

itr = 100
M = 25 # Do 25 x 25 x 25

#### For 3D

a3d = np.zeros(shape=(itr,M,M,M),dtype=int)
# Init the first iteration and reduce the probability of occupancy 
a3d[0] = np.random.choice([0,1],size=(M,M,M), p=[0.0, 1.0]) 

# Reducing the probability of occupancy: 
# p=[0.1, 0.9], p=[0.2, 0.8], p=[0.5, 0.5], p=[0.8, 0.2]
# where p=[x,y] x % zeroes and y % ones

# Test array for directions of movement with M = 2 
# a3d[0] = [[[1, 0],
#          [1, 0]],

#         [[0, 1],
#          [0, 1]]]
1
for i in range(itr-1): #Have to put -1 otherwise we go out of bounds 
    for x in range(M):
        for y in range(M):
            for z in range(M):
                if a3d[i][x][y][z] == 1: #Kills the double occupancy 
                    #print(x,y,z)
                    mov = np.random.randint(6)
                    #Test that directions with the test array
                    #Not necessary though.
                    #mov = 0 #Out of the plane
                    #mov = 1 #Into the plane 
                    #mov = 2 #Move down
                    #mov = 3 #Move up
                    #mov = 4 #Move right
                    #mov = 5 #Move left
                    if mov == 0 and x != 0: 
                        a3d[i+1][x-1][y][z] += 1
                    elif mov == 1 and x != (M-1):
                        a3d[i+1][x+1][y][z] += 1   
                    elif mov == 2 and y != (M-1):
                        a3d[i+1][x][y+1][z] += 1
                    elif mov == 3 and y != 0:
                        a3d[i+1][x][y-1][z] += 1 
                    elif mov == 4 and z != (M-1):
                        a3d[i+1][x][y][z+1] += 1  
                    elif mov == 5 and z != 0:
                        a3d[i+1][x][y][z-1] += 1  
                    else:
                        a3d[i+1][x][y][z] += 1
                    #print()
#print('a3d = \n', a3d)


# Read the number of ones in the matrix of each iteration and append them 
# to an  array to plot no. walkers vs no. iterations

no_arr = np.zeros(shape=(1,itr), dtype=int)
for ii in range(itr):
    for xx in range(M):
        for yy in range(M):
            for zz in range(M):
                if a3d[ii][xx][yy][zz] == 1:
                    no_arr[0][ii] += 1 # Array of number of walkers at every iteration
print('no. walkers at each iteration for testing = \n ', no_arr[0])

"""PLOTS"""
x = np.linspace(1,itr,itr)
t = np.linspace(1, itr, 100, dtype=float) #have to start from t >= 1

# #Plot the number of walkers as a function of time
# plt.title('Number of Viscous Walkers in 3D')
# plt.xlabel('Time (arb. units)')
# plt.ylabel('Number of Walkers')
# plt.plot(x, no_arr.T, label='Stochastic model')

# """Analytical in 3D: rho(t) ~ t**(-1)"""

# plt.plot(t, no_arr[0][0]*t**(-1),label='Analytical model \n'
#           r'$\rho(t) = \rho_0 t^{-1}$')
# plt.legend()
# plt.show()

#Plot the __density__ as a function of time (1 time unit = 1 iteration)

V = M**3
plt.title('Density of Viscous Walkers in 3D')
plt.xlabel('Time (Arb. units)')
plt.ylabel('Density of walkers (1/M^3)')
plt.plot(x, no_arr.T/V, label='Stochastic model')

"""Analytical in 3D: rho(t) ~ t**(-1)"""
plt.plot(t, no_arr[0][0]/V*t**(-1),label='Analytical model \n'
          r'$\rho(t) = \rho_0 t^{-1}$')
plt.legend()
plt.show()

#Log-Log plot of the density
plt.title('log-log plot of the density of Walkers in 3D')
plt.xlabel('Time (arb. units)')
plt.ylabel('Density of Walkers (1/M^3)')
plt.loglog(x, no_arr.T/V, label='Model')
plt.loglog(t, no_arr[0][0]/V*t**(-1), label='Analytical model \n'
          r'$\rho(t) = \rho_0 t^{-1}$')
plt.legend()
plt.show()

# """3D plots of the walkers"""
# #from mpl_toolkits.mplot3d import Axes3D
# #plot a3d[0][:][:][:], a3d[1][:][:][:] and a3d[itr][:][:][:]

# #Initial state
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.voxels(a3d[0][:][:][:], edgecolor="k")
# #set_xticks(np.arange(0, 2, step=1)) # I want one ticks
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.title("Initial State with walkers: " +str(no_arr[0][0]) ) #Try to append the number of walkers here
# plt.show()    

# #Second state
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.voxels(a3d[1][:][:][:], edgecolor="k") #
# #set_xticks(np.arange(0, 2, step=1))
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.title("Second State with walkers = " +str(no_arr[0][1]))
# plt.show()  

# #State in the middle
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.voxels(a3d[int(itr/2)][:][:][:], edgecolor="k") #
# #set_xticks(np.arange(0, 2, step=1))
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.title("Middle state with walkers = " +str(no_arr[0][int(itr/2)]))
# plt.show()  

# #Final state
# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.voxels(a3d[itr-1][:][:][:], edgecolor="k")
# #set_xticks(np.arange(0, 2, step=1))
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# plt.title("Final State with walkers = " +str(no_arr[0][itr-1]))
# plt.show()  
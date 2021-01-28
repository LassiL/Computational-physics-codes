#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 01:12:21 2020

@author: Lassi
"""

"""RANDOM WALKERS IN 2D"""

import numpy as np
import matplotlib.pyplot as plt

""" The 1D code is easily extended to HIGHER DIMENSIONS by increasing the 
dimensions of the initial matrix and the number of random directions for the 
movement. 
    The first index of the matrix is always the no. of iteration."""

itr = 100
M = 300 # Do 100 for the 2D plots and for the graphs

#### For 2D

a2d = np.zeros(shape=(itr,M,M),dtype=int)
# Init a random occupation in 2D lattice for the first iteration
a2d[0] = np.random.choice([0,1],size=(M,M), p=[0.8, 0.2])

# Reducing the probability of occupancy: 
# p=[0.2, 0.8], p=[0.5, 0.5], p=[0.8, 0.2]
# where p=[x,y] x % zeroes and y % ones

# Test matrix for movement for M = 3 (and small itr = 5)
# a2d[0] = [[1, 0, 0], 
#           [0, 1, 1],
#           [0, 0, 1]]

for i in range(itr-1): #Have to put -1 otherwise we go out of bounds 
    for x in range(M):
        for y in range(M):
            if a2d[i][x][y] == 1: #This kills the double occupancy autom.
                #print(x,y)
                mov = np.random.randint(4)
                #Test that directions work correctly before going random
                #mov = 0 #Move up in the matrix 
                #mov = 1 #Move down
                #mov = 2 #Move right
                #mov = 3 #Move left
                if mov == 0 and x != 0: 
                    a2d[i+1][x-1][y] += 1 # Move up (x - 1 = row - 1)
                elif mov == 1 and x != (M-1):
                    a2d[i+1][x+1][y] += 1 # Move down (x + 1 = row + 1)   
                elif mov == 2 and y != (M-1):
                    a2d[i+1][x][y+1] += 1 # Move right (y + 1 = col + 1)
                elif mov == 3 and y != 0:
                    a2d[i+1][x][y-1] += 1 # Move left (y - 1 = col - 1)     
                else:
                    a2d[i+1][x][y] += 1
#print('a2d = \n', a2d)

# Read the number of ones in the matrix of each iteration and append them to 
# an array to plot no. walkers vs no. iterations

no_arr = np.zeros(shape=(1,itr), dtype=int)
for ii in range(itr):
    for xx in range(M):
        for yy in range(M):
            if a2d[ii][xx][yy] == 1:
                no_arr[0][ii] += 1 # Array of no. walkers at every iteration
#print('no. walkers at each iteration for testing = ', no_arr[0])

"""PLOTS"""
x = np.linspace(1,itr,itr) 
t = np.linspace(5, itr, itr, dtype=float) 

# #Plot the __number__ of walkers as a function of time
# plt.title('Number of Viscous Walkers in 2D')

# plt.xlabel('Time (arb. units)')
# plt.ylabel('Number of Walkers')
# plt.plot(x, no_arr.T, label='Stochastic model')

# """Analytical in 2D: rho(t) ~ t**(-1)*log(t)"""
# plt.plot(t, no_arr[0][0]*t**(-1)*np.log(t),label='Analytical model \n'
#           r'$\rho(t) = \rho_0 t^{-1}log(t)$')
# plt.legend()
# plt.show()

#Plot the __density__ as a function of time (1 time unit = 1 iteration)
V = M**2

plt.title('Density of Viscous Walkers in 2D')

plt.xlabel('Time (Arb. units)')
plt.ylabel('Density of walkers (1/M^2)')
plt.plot(x, no_arr.T/V, label='Stochastic model')

"""Analytical in 2D: rho(t) ~ t**(-1)*log(t)"""
plt.plot(t, no_arr[0][0]/V*t**(-1)*np.log(t),label='Analytical model \n'
          r'$\rho(t) = \rho_0 t^{-1}log(t)$')
plt.legend()
plt.show()

#Log-Log plot of the density
plt.title('log-log plot of the density of Walkers in 2D')
plt.xlabel('Time (arb. units)')
plt.ylabel('Density of walkers (1/M^2)')
plt.loglog(x, no_arr.T/V, label='Model')
plt.loglog(t, no_arr[0][0]/V*t**(-1)*np.log(t), label='Analytical model \n'
          r'$\rho(t) = \rho_0 t^{-1}log(t)$')
plt.legend()
plt.show()

# """Plot 2D maps"""
# plt.imshow(a2d[0][:][:])
# plt.colorbar()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title("Initial State with walkers: " +str(no_arr[0][0]))
# plt.set_cmap("Blues_r")
# plt.show()

# plt.imshow(a2d[1][:][:])
# plt.colorbar()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title("Second State with walkers: " +str(no_arr[0][1]))
# plt.set_cmap("Blues_r")
# plt.show()

# plt.imshow(a2d[2][:][:])
# plt.colorbar()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title("Third State with walkers: " +str(no_arr[0][2]))
# plt.set_cmap("Blues_r")
# plt.show()

# plt.imshow(a2d[itr-1][:][:])
# plt.colorbar()
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title("Final state with walkers: " +str(no_arr[0][itr-1]))
# plt.set_cmap("Blues_r")
# plt.show()


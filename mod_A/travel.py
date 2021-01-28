#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 03:28:22 2020

@author: Lassi
"""
import numpy as np
import matplotlib.pyplot as plt

T = 60 * 24
h = 0.1
N_steps = int(T/h)

beta = 0.02
gamma = 0 #consider without vaccination
#gamma = 0.001 
alpha = 1/(14*24)


no_cities = 2

S = np.zeros([no_cities,N_steps+1])
I = np.zeros([no_cities,N_steps+1])
R = np.zeros([no_cities,N_steps+1])

N = np.zeros([no_cities,N_steps+1])

#S[n][i] =  S[city][initial]
S[0][0] = 50000; S[1][0] = 10000; 
I[0][0] = 5000; I[1][0] = 0; 
R[0][0] = 0; R[1][0] = 0;

N[0][0] = S[0][0] + I[0][0] + R[0][0]
N[1][0] = S[1][0] + I[1][0] + R[1][0]


#Satisfy detailed balance: w[n][m]*N[m] = w[m][n]*N[n] 
w = ([0, 0.000005],[9.090909090909092e-07, 0]) 
#w = ([n],[m]) & w[i][i] = 0


for i in range(N_steps):
    for n in range(no_cities):
        N[n][i+1] = S[n][i] + I[n][i] + R[n][i]  
        S[n][i+1] = S[n][i] - h * beta*S[n][i]*I[n][i]/N[n][i] - h*gamma*S[n][i]
        I[n][i+1] = I[n][i] + h * beta*S[n][i]*I[n][i]/N[n][i] - h * alpha*I[n][i]
        R[n][i+1] = R[n][i] + h * alpha*I[n][i] + h*gamma*S[n][i]
        for m in range(no_cities):
            if m!=n:
                S[n][i+1] += h * (w[n][m]*S[m][i]-w[m][n]*S[n][i])
                I[n][i+1] += h * (w[n][m]*I[m][i]-w[m][n]*I[n][i])
                R[n][i+1] += h * (w[n][m]*R[m][i]-w[m][n]*R[n][i])

for n in range(no_cities):
    print('Final population in city', n, '=', int(N[n][i]),'with components: S, I, R = ',
      int(S[n][i]),int(I[n][i]),int(R[n][i]))
    
t = np.linspace(0, N_steps, N_steps+1)*h/24 #in days

for n in range(no_cities):
    plt.plot(t, S[n][:], label = 'S city '+str(n))
    plt.plot(t, I[n][:], label = 'I city '+str(n))
    plt.plot(t, R[n][:], label = 'R city '+str(n))
    #plt.plot(t, N[n][:], label= 'N city '+str(n)) #to see that dN/dt = 0
plt.legend()
plt.xlabel('Days'); plt.ylabel('Amount')
plt.show()
    

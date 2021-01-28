#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:11:39 2020

@author: Lassi
"""

##WITH VACCINATION TO THE MODEL WHERE THE RECOVERY IS NOT PERMANENT

import numpy as np 
import matplotlib.pyplot as plt

T = 60 * 24
h = 0.1
n = int(T/h) #no steps = total_time(Hours)/step_size(Hours)

#Rate constant in units of 1/hours
beta = 0.02
alpha = 1/(14*24) # = 0.00298 (recovery rate 14 days in hours for corona)

gamma = 0.005
#gamma = 0 #no vaccination

#sigma = 0 #permanent immunity
sigma = 1/(90*24) # = 0.000463

S = np.zeros(n+1)
I = np.zeros(n+1)
R = np.zeros(n+1)
V = np.zeros(n+1)

#Initial conditions
S[0] = 50000
I[0] = 5000
# S[0] = 54900
# I[0] = 100

R[0] = 0
V[0] = 0

N = S[0] + I[0] + R[0] + V[0]

#SIR equations with non-permanent immunity in the recovered category, while
#the vaccination gives a permanent immunity (need to implement 4th category)
for i in range(n):
    S[i+1] = S[i] - h * beta*S[i]*I[i]/N - h * gamma*S[i] + h * sigma*R[i] 
    I[i+1] = I[i] + h * beta*S[i]*I[i]/N - h * alpha*I[i]
    R[i+1] = R[i] + h * alpha*I[i] - h * sigma*R[i]
    V[i+1] = V[i] + h * gamma*S[i]
    
    #Check: Detailed balance = 0
    print((S[i+1]+I[i+1]+R[i+1]+V[i+1])-(S[i]+I[i]+R[i]+V[i]))

#𝛽 - rate of infection of susceptible 
#α – rate of recovery of infected
#𝛾 − vaccination of susceptibles turning S into R
#σ - loss of immunity rate
#h - time step in hours

print('Final values: Total population N =', S[i] + I[i] + R[i] + V[i], 
      'with components (S,I,R,V) = ', S[i], I[i], R[i], V[i])

t = np.linspace(0, n, n+1)*h/24 #in days


plt.plot(t, S, label = 'S')
plt.plot(t, I, label = 'I')
plt.plot(t, R, label = 'R')
plt.plot(t, V, label = 'V')
plt.xlabel('Days'); plt.ylabel('Amount')
plt.legend()
plt.show()










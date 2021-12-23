# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:39:51 2021

@author: GLOBAL INFO LAGA
"""

V = [0,0]
R = [0,1]
gamma =1
iteractions = 100000
for i in range (iteractions):
    V [0]= R[0] +gamma*V[1]
    V[1] = R[1]+ gamma*V[0]
    if i%100000 == 0:
        print(V)
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:31:58 2021

@author: GLOBAL INFO LAGA
"""
import numpy as np

Tab = np.random.randint(1,100,10)
print (Tab)

def depiler():
   for i  in range (len(Tab-1),1):
    ind =0
    F = i-1
    while (ind*2+1 <= F):
      pp = ind*2-1
      if((ind+1)*2 <= F and Tab[pp] > Tab[(ind+1)*2]):
        pp = (ind+1)*2
      Tab[ind] = Tab[pp]
      ind = pp
depiler()
print(Tab)
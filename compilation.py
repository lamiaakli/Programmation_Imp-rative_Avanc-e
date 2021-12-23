# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:37:49 2021

@author: GLOBAL INFO LAGA
"""
import copy
import math

class Noeud():
    def __init__(self, D, G, val=math.inf):
        self.G = G
        self.D = D
        self.val = val
    def isFeuille(self):
        if self.D == None and self.G == None:
            return True
        return False
    
V = [7,9,5,4,11,13,4,17,5,9,4,3,11,1,13,6]

def createTree(V):
    Nd = []
    for i in range(len(V)):
        Nd.append(Noeud(None,None, V[i]))
    continu = True
    while(continu):
        Parents =[]
        for i in range(0,len(Nd),2):
            Parents.append(Noeud(Nd[i], Nd[i+1]))
        if len(Parents)==1 :
            continu = False
        else:
            Nd =copy.deepcopy(Parents)
            Parents.clear()
    return Parents[0]
    
def printTree(N):
    if N.isFeuille()==True:
        print(N.val,end=",")
    else:
        printTree(N.G)
        printTree(N.D)
        
        

def elagage(N, depth=0, alpha=math.inf, beta= math.inf):
    if N.isFeuille():
        return N.val
    successeurs = [N.G, N.D]
    if(depth%2) == 0:
       MaxValue = math.inf
       for s in  successeurs:
           value = elagage (s, depth+1, alpha, beta)
           MaxValue = max(MaxValue,value)
           alpha = max(alpha,value)
           if(beta <= alpha): break
       return MaxValue
    else:
       MinValue =math.inf
       for s in successeurs:
           value = elagage(s, depth+1, alpha, beta)
           MinValue = min(MinValue,value)
           beta = min(beta,value)
           if (beta <= alpha): break
       return MinValue
        
    A = createTree(V)
    printTree(A)

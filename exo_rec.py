# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 09:13:51 2021

@author: GLOBAL INFO LAGA
"""


import numpy as np
import sys
import copy

def lireReseau ():
    Reseau = np.loadtxt("reseau.txt", dtype=int)
    sommets = []
    for i in range (len(Reseau)):
        sommets.append("S"+str(i))
    return Reseau, sommets
Reseau, sommets = lireReseau()

PccCh = []
PccKm = sys.maxsize

Ch = []
Km = 0

def Rechercher(D,A):
    """fonction pour rechercher le plus court chemin"""
    global PccCh, PccKm, Ch,Km
    if D == A:
        PccCh = copy.deepcopy(Ch)
        PccKm = Km
    indD = sommets.index(D)
     
    for V in [S for S in sommets if S not in Ch]:      
          indV = sommets.index(V)
          if Reseau [indD,indV] > 0 and PccKm > Km + Reseau[indD, indV]:
              
            Ch.append(V)
            Km += Reseau[indD,indV]
            Rechercher(V,A)
            del Ch[-1]
            Km -= Reseau[indD, indV]
            
D = "S0"
A = "S5"
Ch.append(D)
Rechercher(D, A)
print(PccCh)
print(PccKm)
          





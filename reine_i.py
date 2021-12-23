# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 10:34:07 2021

@author: GLOBAL INFO LAGA
"""

Taille = 8
TableDesReines = [0]*Taille

#Chercher solution

def estacceptable(e, numReine):
    if e in TableDesReines[0:numReine]:
        return False
    for i in range(numReine):
        if abs(numReine-1) == abs(e-TableDesReines[i]):
            return False
        return True
def placement_reine(numReine):
    Trouve = False
    if(numReine == len(TableDesReines)):
        Trouve = True ; return
    for e in range(Taille):
        if estacceptable(e, numReine):
            TableDesReines[numReine] = e
            placement_reine(numReine + 1)
            if Trouve : return
            TableDesReines[numReine] = 0
            
placement_reine(0)

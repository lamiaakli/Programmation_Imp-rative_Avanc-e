# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 20:28:35 2021

@author: GLOBAL INFO LAGA
"""
"""
- les cases avec un 1 sont des murs => '#'
- les cases avec un 0 sont des espaces vides => ' '
    """
def labyrinthe(tab):
    
    for j in range(0,len(tab[0])):
       for i in range(0,len(tab)):
            if(tab[i][j]==1):
                print ("#", end = ' ')
            else: 
                print(" ", end = ' ')
       print()
       
       
def transpose(laby):
    """
    permet d'inverser lignes et colonnes d'un labyrinthe
    (utile pour la creation simple)
    """
    # nouveau laby
    laby2=[]
    for i in range(0,len(laby[0])):
        ligne=[]
        for j in range(0,len(laby)):
            ligne+=[0]
        laby2+=[ligne]

    # transposition
    for i in range(0,len(laby[0])):
        for j in range(0,len(laby)):
            laby2[i][j]=laby[j][i]

    return laby2
       
def getlaby():
    
    laby = []
    laby +=[[1,1,1,1,1,1,1,1]]
    laby +=[[1,0,0,1,0,0,0,1]]
    laby +=[[1,0,0,1,0,1,0,1]]
    laby +=[[1,0,1,1,1,1,0,1]]
    laby +=[[1,0,0,0,0,0,0,1]]
    laby +=[[1,1,0,1,1,0,1,1]]
    laby +=[[1,0,0,0,0,0,0,1]]
    laby +=[[1,1,1,1,1,1,1,1]]

    return transpose(laby)

def getlaby():
    return (4,6)


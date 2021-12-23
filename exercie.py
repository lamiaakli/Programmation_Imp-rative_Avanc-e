# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:10:41 2021

@author: GLOBAL INFO LAGA
"""
#QST1
N = 6
def somme(N) :
    if (N == 1) : #condition d'arret
        return 1
    else:     
        return N + somme(N - 1)
  
   
print(somme(N))

#QST2
n = 0

def unZero(n):
    if (n < 10):
        return n == 0
    elif  (n % 10) == 0 :
          return 1
    else :
        unZero(n//10)
print(unZero(n))

#QST3

def puis(x,n):
    if n == 1:
        return x
    else:
       p = puis(x, n//2)
       if(n%2 == 0):
           return p*p
       else:
           return p*p*x
       
               
print(puis(2,10))
        
#QST4

def distance (x,debut, fin):
     
    if (fin == debut):
        return x-t[debut]
    else:
       return  min(x-t[debut], distance(x, debut+1, fin))
        
        
print(distance(3,2,20))




        
# Programme pour générer la suite de Fibonacci en utilisant la récursivité
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Entrez le nombre de termes:"))
print("Suite de Fibonacci en utilisant la recursion :")
for i in range(n):
    print(fibonacci(i))

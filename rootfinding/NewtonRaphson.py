# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:25:23 2022

@author: rjara
"""

def f(x):
    return -(x**2+(3*x))             #(x**5)-x-1

def fp(x):
    return -2*x-3             #(5*x**4)-1

#%%

def NewtonRaphson(a, tolx, toly):
    
    k=0
    b= a - (f(a)/fp(a))
    
    print(f"El intervalo es {a}, {b}" )
    
    while (abs(b-a)>tolx) or (abs(f(b)-f(a))>toly):
        
        a=b
        
        b = a - (f(a)/fp(a))
        
        print(k)
        print(f"El intervalo es {a}, {b}" )
        
        k=k+1
    
    print('x=',k-1, '=',round(b,8), 'es una aproximacion valida')
    
print(NewtonRaphson(-2,10**-6,10**-6))

#%%

#EJERCICIOS 

#a

import math


def f(x):
    return  1 - 2*x*math.exp(-x/2)


























        
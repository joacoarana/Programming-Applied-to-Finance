# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 19:07:24 2022

@author: rjara
"""

def f(x):
    return -(x**2+(3*x))             #-(x**3)/(2*x+1)    #(1/x) -1

funcion= str(input('decreciente o creciente:'))


def aproximacion_sucesiva(a, alpha, tol):
    
    k=1
    b=a+1
    
    while (abs(a-b)>tol):
        
        if funcion== 'creciente':
            
            if f(a)<0:
                m = a + (1*alpha/k)
            if f(a)>0:
                m = a - (1*alpha/k)
                
        if funcion== 'decreciente':
            
            if f(a)>0:
                m = a + (1*alpha/k)
            if f(a)<0:
                m = a - (1*alpha/k)
        b=a
        a=m
        
        print(k)
        print(f"El intervalo es {a}, {b}" )
        
        k=k+1
        
        
        
    print('x=',k-1, '=',(m), 'es una aproximacion valida')
    
print(aproximacion_sucesiva(-0.5,1,10**-6))

#%%

def f(x):
    return -(x**2+(3*x))             #-(x**3)/(2*x+1)    #(1/x) -1

funcion= str(input('decreciente o creciente:'))


def aproximacion_sucesiva(a, alpha, tol):
    
    k=1
    b=a+1
    
    print(f"El intervalo es {a}, {b}" )
    
    while (abs(a-b)>tol):
        
        if funcion== 'creciente':
            
            if f(a)<0:
                m = a + (1*alpha/k)
            if f(a)>0:
                m = a - (1*alpha/k)
                
        if funcion== 'decreciente':
            
            if f(a)>0:
                m = a + (1*alpha/k)
            if f(a)<0:
                m = a - (1*alpha/k)
        b=a
        a=m
        
        print(k)
        print(f"El intervalo es {a}, {b}" )
        
        k=k+1
        
        
        
    print('x=',k-1, '=',(m), 'es una aproximacion valida')
    
print(aproximacion_sucesiva(-0.5,1,10**-6))
    
    
    
    
    
    
    
        
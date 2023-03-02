# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 13:36:31 2022

@author: rjara
"""

def f(x):
    return  (x**2)-4

def biseccion(a,b,tol):
   
    k=0
    
    if f(a)*f(b)>0:
        print ('No tiene raiz')
    
    while(abs(a-b)>tol):     
       
       m = (a+b)/2
        
       if (f(a)*f(m)<0):
            b=m
            
       if (f(b)*f(m)<0):
            a=m     
               
       print(f"El intervalo es {a}, {b}" )
        
       k= k+1
        
    return m   
    print('x=',k, '=',m, 'es una aproximacion valida')

biseccion(-3,-1.5,10**-6)


#%%

def f(x):
    return  (x**2)-4

def biseccion(a,b,tol):
    m1=a
    m=b
    k=0
    
    if f(a)*f(b)>0:
        print ('No tiene raiz')
    
    while(abs(m1-m)>tol):
       m1=m     
       
       m = (a+b)/2
        
       if (f(a)*f(m)<0):
            b=m
            
       if (f(b)*f(m)<0):
            a=m     
               
       print(f"El intervalo es {a}, {b}" )
        
       k= k+1
        
        
    print('x=',k, '=',m, 'es una aproximacion valida')

print(biseccion(-3,-1.5,10**-6))

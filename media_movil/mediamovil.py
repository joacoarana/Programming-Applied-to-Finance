# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 17:12:01 2022

@author: rjara
"""

import ffn 
import pandas
import matplotlib.pyplot as plt

prices = ffn.get('msft:Close,msft', start='2022-06-25', end='2022-06-29')

variacion_precios_diarios= ffn.get('msft:Close,msft', start='2010-01-01').to_returns().dropna()

#print(prices)
#print(variacion_precios_diarios)

#tenemos que tener las formas lineales y logaritmicas 

#%%

def media_movil_simple(precios,n):
    x=len(precios)
    p=x-n+1
    media=[]
    for i in range (p):
        value=0
        for a in range(n):
            value+=precios[a+i]
        media.append(value/n)
    return media

def media_movil_ponderada(precios,n):
    x=len(precios)
    p=x-n+1
    media=[]
    for i in range (p):
        value=0
        denominador=0
        for a in range(n):
            value+=precios[a+i]*(a+1)
            denominador+= a+1
        media.append(value/denominador)
    return media

def media_movil_exponencial(precios,n):
    x=len(precios)
    p=x-n+1
    k=2/(n+1)
    media=[]
    for i in range(p):
        if i==0:
            value=0
            for a in range(n):
                value+=precios[a]
            media.append(value/n)
        else:
            media.append(precios[i]*k+media[i-1]*(1-k))
            
    return media
    

#%%
if __name__=="__main__":
    #precios=[1,1,2,1,2]
    precios= prices['msftclose']
    x=media_movil_simple(precios,2)
    print(x)
    
    #y=media_movil_ponderada(precios,2)
    #print(y)
    
    tiempo=[x for i,x in enumerate(prices.index)]
    print(tiempo)
    plt.plot(tiempo,precios)
    
    precios=prices['msft']
    z=media_movil_exponencial(precios, 2)
    print(z)
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 10:56:10 2022

@author: rjara
"""
#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datetime

import pandas_datareader as pdr
import pandas_datareader.data as web
import math as m
#%%
inicio= datetime.datetime(2015, 6, 9)
fin= datetime.datetime(2020, 6, 9)

Apple= web.DataReader('AAPL','yahoo',inicio, fin)
#%%
def mmovil(n, precios):
    promedios=[0]*(n-1)
        
    for i in range(n-1, len(precios)):
        suma = 0
        for k in range (n):
            suma += precios[i-k]
        a = suma/n
        promedios.append(a)
    
    return promedios

def mmponderada(n, precios):
    promedios=[0]*(n-1)
        
    for i in range(n-1, len(precios)):
        suma = 0
        denominador=0
        for k in range (n):
            suma += precios[i-k] *(n-k)
            denominador= denominador + (n-k)
            
        a = suma/denominador
        promedios.append(a)
    return promedios

def EMA(n, precios):
    promedios=[0]*(n-1)
    k=2/(n+1)
    
    for i in range(n-1, len(precios)):
        if i ==n-1:
            suma=0
            for j in range(n):
                suma += precios[j]
            a= suma/n
            promedios.append(a)
            print(promedios)        
        else:
            promedios.append((precios[n-2 +i])*k+promedios[n-3+i]*(1-k))
            print(promedios)
    return promedios


x=[3,4,2,8,9,4,4,12,5,7,9]

EMA(2, x)

def graficar(precios, mm, x):
    
    plt.style.use("seaborn")
    plt.plot(x, p, "black")
    plt.plot(x,mm, "orange")
    
#%%
p= list(Apple.Close)
p
x= Apple.index

mm= mmponderada(100, p)
mm

graficar(p, mm,x)


    


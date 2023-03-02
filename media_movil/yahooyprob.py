# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 18:24:34 2022

@author: rjara
"""

pip install pandas_datareader

inicio.__doc__
#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import datetime

import pandas_datareader as pdr
import pandas_datareader.data as web
import math as m

#%%
def Lag (entrada, nlags=1):
    salida=[0]*nlags+entrada[0:len(entrada)-nlags]
    return salida

def daily_return (entrada):
    aux= Lag(entrada)
    retornos = []
    for n in range (0,len(aux)):
        if aux[n] != 0:
            retornos.append((entrada[n]-aux[n])/aux[n])
        
    return retornos

def media_m(entrada):
    N= len(entrada)
    suma = 0
    for i in range(len(entrada)):
        suma= suma + entrada[i]
        
    media = suma/N
    return media

def varianza1_p(entrada):
    xraya = media_m(entrada)
    aux= [i**2 for i in entrada]
    ex2= media_m(aux)
    vari= ex2-xraya**2
    return vari

def varianza2_p(entrada):
    xraya = media_m(entrada)
    aux= [(i-xraya)**2 for i in entrada]
    vari= media_m(aux)
    return vari
        
def desv1_p (entrada):
    return(varianza1_p(entrada))**0.5
    
def desv2_p (entrada):
    return(varianza2_p(entrada))**0.5    
    
def asimetría(entrada):
    xraua = media_m((entrada))
    sigma= desv1_p(entrada)
    aux= [((i-xraya)/sigma)**3 for i in entrada]
    coef_asimetria= media_m(aux)
    return coef_asimetria

def curtosis(entrada):
    xraua = media_m((entrada))
    sigma= desv1_p(entrada)
    aux= [((i-xraya)/sigma)**4 for i in entrada]
    coef_curtosis= media_m(aux)
    return coef_curtosis

    
#%%

inicio= datetime.datetime(2015, 6, 9)
fin= datetime.datetime(2020, 6, 9)


Apple= web.DataReader('AAPL','yahoo',inicio, fin)

Apple.Open

Close_Apple= list(Apple.Close)
Close_Apple

daily_return (Close_Apple)
media_m(Close_Apple)















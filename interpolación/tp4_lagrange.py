# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import sys
sys.path

# path a modulos
path="C:/Users/rjara/OneDrive/Desktop/Programación Finanzas/tp4" 
if not(path in sys.path):
    sys.path.append(path)

# import numpy as np (builtin)
import importlib
bp = importlib.import_module(name ="basa_poly")
#%%

import math as m
import math
import numpy as np
import matplotlib.pyplot as plt


m.sin(m.pi/2)


#%%

def listas(fx,a,b,k):
    distancia=b-a
    m=a

    xlist= [a]
    ylist= [fx(a)]
    
    while m<b:
        m= m+ distancia/(k-1)
        if m <=b:
            #print(m)
            xlist.append(m)
            ylist.append(fx(m))
    return xlist, ylist

def interpolacion_polinomica(xval,xdat,ydat):
    p = 0
    M = len(xdat)
    for j in range(0, M):
        xj = xdat[j]
        l = 1
        for i in range(0, M):
            xi = xdat[i]
            if(i != j):
                l = l * ((xval - xi) / (xj - xi))
                #print(xval-xi)
                
        p = p + ydat[j] * l
        #print(p)
        
    return p
#%% EJERCICIO 2

values= listas (m.sin,-m.pi/2, m.pi/2, 11)

y1 = np.array(values[1])
x1 = np.array(values[0])

xvals = np.linspace(-m.pi/2, m.pi/2)
xvals

yvals = interpolacion_polinomica(xvals,x1,y1)
plt.plot(xvals, yvals, color = 'blue')
plt.show()

#%% EJERCICIO 3a

values2= listas (m.exp,-2, 2, 11)

y2 = np.array(values2[1])
x2 = np.array(values2[0])

xvals2 = np.linspace(-2,2)
xvals2

yvals2 = interpolacion_polinomica(xvals2,x2,y2)
#plt.plot(xvals2, yvals2, color = 'blue')
#plt.show()

#%% 3b

values3= listas (m.exp,1, 3, 11)

y3 = np.array(values3[1])
x3 = np.array(values3[0])

xvals3 = np.linspace(1,3)
xvals3

yvals3 = interpolacion_polinomica(xvals3,x3,y3)
#plt.plot(xvals3, yvals3, color = 'red')
#plt.show()
#%%
plt.plot(xvals, yvals, color = 'orange')
plt.plot(xvals2, yvals2, color= "blue")
plt.plot(xvals3, yvals3, color= "red")
plt.show()










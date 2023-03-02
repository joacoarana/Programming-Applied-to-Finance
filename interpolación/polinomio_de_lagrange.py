#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 18:10:34 2022

@author: rjara
"""
import math
import numpy as np
import matplotlib.pyplot as plt



y1 = np.array([1,0,1])
x1 = np.array([-1,0,1])


xvals = np.linspace(-1,1)
xvals

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
yvals1 = interpolacion_polinomica(xvals, x1, y1)
plt.plot(xvals, yvals1, color = 'blue')
plt.show()


print(yvals1)
#%%
#Ejercicio 2
values = listas(m.sin,-m.pi/2,m.pi/2,11)
x1 = np.array(values[0])
y1 = np.array(values[1])

xvals = np.linspace(-m.pi/2,m.pi/2)
yvals = interpolacion_polinomica(xvals, x1, y1)
plt.plot(xvals, yvals, color = 'blue')
plt.show()
#Ejercicio 3
values1 = listas(m.exp,-2,2,3)
x2 = np.array(values1[0])
y2 = np.array(values1[1])

xvals1 = np.linspace(-2,2)
yvals1 = interpolacion_polinomica(xvals1, x2, y2)
plt.plot(xvals1,yvals1,color = 'red')

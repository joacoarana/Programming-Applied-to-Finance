# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 23:09:45 2022

@author: rjara
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
import numpy as np
import matplotlib.pyplot as plt

def Find_abc(x,y,b1):
    b_list = [0,b1]
    a_list = []
    c_list = []
    for i in range(len(x)-2):
        b_list.append(3*(((y[i+2]-y[i+1])/(x[i+2]-x[i+1]))-((y[i+1]-y[i])/(x[i+1]-x[i])))/((x[i+2]-x[i+1]))-(2*(b_list[i+1])*((x[i+1]-x[i])+(x[i+2]-x[i+1]))/(x[i+2]-x[i+1]))-((b_list[i])*((x[i+1]-x[i])/(x[i+2]-x[i+1]))))
    for i in range(len(x)-1):
        if i != len(x)-2:
            a_list.append((b_list[i+1]-b_list[i])/3/(x[i+1]-x[i]))
        elif i == len(x)-2:
            a_list.append(-b_list[i]/(3*(x[i+1]-x[i])))
    for i in range(len(x)-1):
        c_list.append(((y[i+1]-y[i])/(x[i+1]-x[i]))-((b_list[i])*(x[i+1]-x[i]))-((a_list[i])*((x[i+1]-x[i])**2)))
    return a_list,b_list,c_list


def My_b(x,y,b1,n): 
    if n==0:
        return 0
    elif n==1:
        return b1
    else:
        i = n-2
        return (3*(((y[i+2]-y[i+1])/(x[i+2]-x[i+1]))
                   -((y[i+1]-y[i])/(x[i+1]-x[i])))/((x[i+2]-x[i+1]))
                -(2*(My_b(x,y,b1,n-1))*((x[i+1]-x[i])+(x[i+2]-x[i+1]))/(x[i+2]-x[i+1]))
                -((My_b(x,y,b1,n-2))* ((x[i+1]-x[i])/(x[i+2]-x[i+1]))))
    
def rootfinder_b(x,y, tol, nmax,h):
    n = 0
    sets = [1]
    b1 = 0
    bn = My_b(x, y, b1, len(x)-1)
    while abs(bn)>tol and n<nmax:
        n += 1
        bn = My_b(x, y, b1, len(x)-1)
        if len(x)%2 == 0:
            if bn < 0:
                sets.append(1)
            else:
                sets.append(-1)
        else:
            if bn > 0:
                sets.append(1)
            else:
                sets.append(-1)
        if sets[n] != sets[n-1]:
            h = h*0.5
            h = -h
        b1 = b1 + h
        
    return b1

def armar_polinomios(x,y,b1):
    polys_c = Find_abc(x, y, b1)
    polys = [bp.basa_poly([polys_c[0][i],polys_c[1][i],polys_c[2][i],y[i]]) for i in range(len(y)-1)]
    return polys

def plot_split_function(x,y,polys):
    for i in range(len(polys)):
        x_plot0 = np.linspace(0,x[i+1]-x[i],50)
        x_plot1 = np.linspace(x[i],x[i+1],50)
        y_plot0 = []
        for p,q in enumerate(x_plot0):
            y_plot0.append(polys[i].f(q))
        plt.style.use("seaborn")
        plt.plot(x_plot1,y_plot0)
    plt.plot(x,y,'o',color='black')

def plot_set(x,y):
    plt.plot(x,y,"o",color = "black")

def sort_x_y(x,y):
    x_copy = x.copy()
    y_copy = []
    x_copy.sort()
    for i in range(len(x)):
        y_copy.append(y[x.index(x_copy[i])])
    return x_copy,y_copy

def valor_tasa(lista_polinomios, xi, valor_x): #valor_x tiene que ser >= a xi[0]
    
    for i in range (1, len(xi)):
        if xi[i-1]< valor_x <= xi[i]:
            tasa= lista_polinomios[i-1].f(valor_x-xi[i-1])
            
        if valor_x == xi[0]:
            tasa = lista_polinomios[0].f(0)
            
    return tasa

def BPS_addition (spot_curve, bps):
    for i in range(len(b)):
        spot_curve[i]+= bps/10000
    return spot_curve


def Valuar_Flujos (flujos, x_flujos, lista_polinomios, xi):  #xi, x_flujos en años
    va=[]
    for i in range(len(flujos)):
        tasa0coupon = valor_tasa(lista_polinomios, xi, x_flujos[i])
        
        a= flujos[i]/ ((1+tasa0coupon)**x_flujos[i])
        va.append(a)
    return va




#%%

class xy:
    def __init__(self, x, y):
        if self.repeat_checker(x) == True:
            raise ValueError ("Hay dos valores de x iguales..")
        else:
            set_xy = list(zip(x, y))
            set_xy = sorted(set_xy, key = lambda x: x[0])
            self.x = [i[0] for i in set_xy]
            self.y = [i[1] for i in set_xy]
            
    def repeat_checker(self, x):
        l = list()
        for i in x:
            if i not in l:
                l.append(i) 
            else:
                return True

    def spot_curve(self, spots, year):
            
        yields = self.y.copy()
    
        if year == yields[0]:
            spots.append(yields[0])
            return yields[0]
        else:
            rate = yields[year-1]
            numerador = 1 + rate
            denom = []
            for i in range(1,year):
                fraccion = rate / ( (1 + spots[i-1])**i )
                denom.append(fraccion)
            denominador = 1 - sum(denom)
            spot_rate = ((numerador/denominador)**(1/year)) - 1
            spots.append(spot_rate)
        return spot_rate
            
    def get_spot_curve(self):
        madurez = self.x.copy()
        spots = []
        year = 1
        while year <= len(madurez):
            self.spot_curve(spots, year)
            year += 1
        return spots    
    
#x= [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
#y= [5,4,3,2,1,0,1,2,1,0,1,0,1,2,1,0,1,2,3,4,5]    

#rootfinder_b(x, y, 0.00001, 1000, 1)        

#%%PAR YIELD

xi_monthly= [1, 2, 3, 6, 12,24,36,60,84,120,240,360]
xi= [1/12, 2/12, 3/12, 6/12, 1,2,3,5,7,10,20,30]
yi=[0.00634, 0.008833, 0.0101635, 0.014756, 0.0204955, 0.025848, 0.027335, 0.0280515, 0.0282115, 0.027874, 0.031766, 0.029924]

b1= rootfinder_b(xi, yi, 0.00001, 10000, 0.1)
b1

polinomios=armar_polinomios(xi, yi, b1)
plot_split_function(xi,yi,polinomios)

polinomios[10].f(10)

valor_tasa(polinomios, xi, 8.5)

#%%SPOT CURVE
a= xy(xi_monthly, yi)
b= a.get_spot_curve()
print(b)

b_1= rootfinder_b(xi, b, 0.00001, 10000, 0.1)
b_1  

b= BPS_addition(b, 285)
    
polinomios_spot= armar_polinomios(xi, b, b_1)
plot_split_function(xi,b,polinomios_spot)

flujos= [8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75, 8.75,  8.75, 1008.75]
x_flujos=[0.5, 1,1.5,2, 2.5,3 ,3.5,4,4.5,5,5.5,6,6.5,7, 7.5, 8, 8.5, 9, 9.5]

resultado = Valuar_Flujos(flujos, x_flujos, polinomios_spot, xi)

resultado

clean = sum(resultado)
    
acc_interest= (65/360) *1000 * 0.00875      

dirty = clean + acc_interest

# EL 20 DE MAYO:
    
dirty

#%%  
        
        
        
        
        
        
        
        
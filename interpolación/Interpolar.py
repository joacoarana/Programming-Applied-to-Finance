#%%%%
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('C:\\Users\Marcelo\Desktop\Programación AF\Archivos')

from matrix import Matrix
import Interpolar
import fechas
from basa_poly import basa_poly
from Curve import Curve

import importlib
curve = importlib.import_module(name ="Curve")

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


#%%%
 
def Lagrange_interpolation(xlist,ylist):
    counter_poly = basa_poly([np.float64(0)])
    for i in range(len(xlist)):     
        counter = basa_poly([1])           
        for x in range(len(xlist)):
            if x == i:
                counter *= basa_poly([np.float64(ylist[x])]) 
            elif ylist[i] != 0:       
                counter *= basa_poly([1,-xlist[x]])//basa_poly([np.float64(xlist[i]-xlist[x])])
            elif ylist[i] == 0:                      
                counter *= basa_poly([0])
        counter_poly += counter       
    return counter_poly.destroyer(4)


#%%%

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
    if n == 0:
        return 0
    elif n == 1:
        return b1
    else:
        i = n-2
        return (3*(((y[i+2]-y[i+1])/(x[i+2]-x[i+1]))
                   -((y[i+1]-y[i])/(x[i+1]-x[i])))/((x[i+2]-x[i+1]))
                -(2*(My_b(x,y,b1,n-1))*((x[i+1]-x[i])+(x[i+2]-x[i+1]))/(x[i+2]-x[i+1]))
                -((My_b(x,y,b1,n-2))*((x[i+1]-x[i])/(x[i+2]-x[i+1]))))
    
def Cubic_Splines_Interpolation(x,y):
    tol = 0.000001
    n = 0
    nmax = 100
    h = 10
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


#%%

xi= [1/12, 2/12, 3/12, 6/12, 1,2,3,5,7,10,20,30]
yi=[0.00634, 0.008833, 0.0101635, 0.014756, 0.0204955, 0.025848, 0.027335, 0.0280515, 0.0282115, 0.027874, 0.031766, 0.029924]

a= Cubic_Splines_Interpolation(xi, yi)
len(a)

a[0].f(0)



#%%%%%

def switch_row(matrix,row0,row1):
    row1_c = matrix[row1].copy()
    matrix[row1] = matrix[row0].copy()
    matrix[row0] = row1_c
    


def print_matrix(matrix):
    for i in range(len(matrix)):
        print("|",end=" ")
        for x in range(len(matrix[0])-1):
            print(matrix[i][x],end=" ")
        print("|", end="   ")
        print("|",matrix[i][-1],"|")
        
def Get_Interpolation_Matrix(x1,y1,type_c="B0-BN"):
    matrix = []
    
    if type_c == "CUADRATIC":
        for i in range(len(x1)-1):
            Dx = x1[i+1] - x1[i]
            Dy = y1[i+1] - y1[i]
            if i != len(x1)-2:
                for x in range(3):
                    if x == 0:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(Dx**3),row.append(Dx**2),row.append(Dx)
                        for z in range((len(x1)-2-i)*3):
                            row.append(0)
                        row.append(Dy)
                        matrix.append(row)
                    elif x == 1:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(3*(Dx**2)),row.append(2*Dx),row.append(1)
                        row.append(0),row.append(0),row.append(-1)
                        for z in range((len(x1)-3-i)*3+1):
                            row.append(0)
                        matrix.append(row)
                    elif x == 2:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(6*Dx),row.append(2),row.append(0)
                        row.append(0),row.append(-2),row.append(0)
                        for z in range((len(x1)-3-i)*3+1):
                            row.append(0)
                        matrix.append(row)
            if i == len(x1)-2:
                for x in range(3):
                    if x == 0:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(Dx**3),row.append(Dx**2),row.append(Dx)
                        row.append(Dy)
                        matrix.append(row)
                    if x == 1:
                        row = []
                        row.append(1),row.append(0)
                        for z in range((len(x1)-2)*3+2):
                            row.append(0)
                        matrix.append(row)
                    if x == 2:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(1),row.append(0),row.append(0),row.append(0)
                        matrix.append(row)
    elif type_c == "B0-BN":
        for i in range(len(x1)-1):
            Dx = x1[i+1] - x1[i]
            Dy = y1[i+1] - y1[i]
            if i != len(x1)-2:
                for x in range(3):
                    if x == 0:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(Dx**3),row.append(Dx**2),row.append(Dx)
                        for z in range((len(x1)-2-i)*3):
                            row.append(0)
                        row.append(Dy)
                        matrix.append(row)
                    elif x == 1:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(3*(Dx**2)),row.append(2*Dx),row.append(1)
                        row.append(0),row.append(0),row.append(-1)
                        for z in range((len(x1)-3-i)*3+1):
                            row.append(0)
                        matrix.append(row)
                    elif x == 2:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(6*Dx),row.append(2),row.append(0)
                        row.append(0),row.append(-2),row.append(0)
                        for z in range((len(x1)-3-i)*3+1):
                            row.append(0)
                        matrix.append(row)
            if i == len(x1)-2:
                for x in range(3):
                    if x == 0:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(Dx**3),row.append(Dx**2),row.append(Dx)
                        row.append(Dy)
                        matrix.append(row)
                    if x == 1:
                        row = []
                        for z in range(i*3):
                            row.append(0)
                        row.append(6*Dx),row.append(2),row.append(0)
                        row.append(0)
                        matrix.append(row)
                    if x == 2:
                        row = []
                        row.append(0),row.append(1)
                        for z in range((len(x1)-2)*3+2):
                            row.append(0)
                        matrix.append(row)
                        
    copy_m = [row[:-1] for row in matrix]
    copy_i = [row[-1:] for row in matrix]

    return copy_m,copy_i
            
def Cubic_Splines_Interpolation_byMatrix(x1,y1,res_t="B0-BN",printout=0):
    mr = Get_Interpolation_Matrix(x1, y1,res_t)
    mM = Matrix(mr[0])
    mI = Matrix(mr[1])
    solved = mM.invert_m().matrix_op(mI,"mul").matrix
    if printout == 0:
        polyz = []
        for i in range(len(x1)-1):
            poly = []
            for x in range(4):
                if x != 3:
                    poly.append(solved[(3*i)+x][0])
                elif x == 3:
                    poly.append(y1[i])
            polyz.append(basa_poly(poly))
        return polyz
    
    
def Number_Cleaner(number,decimals):
    tol = 0.0001
    if abs(number - int(number)) < tol:
        return int(number)
    else:
        return np.round(number,decimals)
        
def Matrix_cleaner(matrix,decimals):
    for x in range(len(matrix)):
        for z in range(len(matrix[0])):
            matrix[x][z] = Number_Cleaner(matrix[x][z],decimals)
            

#%%




# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 18:40:15 2022

@author: rjara
"""

import numpy as np
def det(M):
    cofactor=0
    n=len(M)
    if n==2:
        cofactor = M[0][0] * M[1][1] - M[0][1] * M[1][0]
        return cofactor
    
   
    for j in range(n): 
   
        Mx = M.copy() 
        Mx = Mx[1:]
        n2=len(Mx) 
        for i in range(n2): 
            Mx[i] = Mx[i][0:j] + Mx[i][j+1:] 
        cofactor += ((-1) ** (1+j+1))*M[0][j] *det(Mx)
    return cofactor
    
def matriz_traspuesta(matriz):
    m_traspuesta = []
    M = len(matriz)
    
    for i in range(M):
        line = []
        for j in range(M):
            line.append(matriz[j][i])
            
        m_traspuesta.append(line)
    return m_traspuesta

def columna(M,j):
    return [M[i][j] for i in range(len(M))]

def fila(M,j):
    return [M[i][j] for i in range(len(M))]

#columna([[1, 2, 8], [2, 3, 2], [3, 2, 3]], 0)
        
def zero_matrix(n,j):
    fila_1 = [0 for i in range(n)]
    return [fila_1.copy() for i in range(j)]
    
def vector_x_vector(N, M):
    return sum([x*y for x,y in zip(N, M)])

#vector_x_vector([1,2,8], [1,1,1])

def square_matrix(a):
    if len (a)==len (a[0]):
        return "cuadrada"
    else:
        return "no cuadrada"

def multiplicacion_matrices(a,b):
    #if square_matrix(a) == "cuadrada":
     #   pass
    #elif square_matrix(b) == "cuadrada":
     #   pass    
    #else:
     #   return "Alguna matriz no es cuadrada"
    
    n= zero_matrix(len(b[0]), len(a))
    
    nro_columnas=len(b[0])
    
    nro_filas= len(a)
    
    
    for i in range(0, nro_filas):        
        m= a[i]
        
        for j in range(0, nro_columnas):            
            k= columna(b, j)           
            n[i][j]=( vector_x_vector(m, k))
    return n

def identidad (l):
    n=zero_matrix(l, l)
    
    for i in range (l):
        n[i][i]=1
    return n

def swap_columns (a,b,l):
    n= identidad (l)
    new_matrix= zero_matrix(l, l)
    
    for i in range (l):
        p = columna(n, i)
        new_matrix[i]=p
        
    new_matrix[a], new_matrix[b] = new_matrix[b], new_matrix[a]
    
    for i in range (l):
        q = columna(new_matrix, i)
        new_matrix[i]=q
        
    return new_matrix
    
def swap_filas (a,b,l):
    n= identidad (l)
        
    n[a], n[b] = n[b], n[a]
        
    return n   
swap_columns(1, 3, 4)
swap_filas(1, 3, 4)        
    
    

def inversa(M):
    
    a= len(M)
    i_list =[]
    i= identidad(a)
    normalizar_list=[]
    resta_list=[]

    for n in range (0, a):

        if M[n][n] == 0:
            t=[]
            for k in range (n+1,a):
                if M[n][k] != 0:
                    t=swap_columns(0, k, a)
                else:
                    t= []
                
                if t != []:
                    break
                else:
                    pass
                
            if t == []:                
                print("Matriz no inversible")
                break
                
            else:
                i_list.append(t)
                
            M= multiplicacion_matrices(M, t)
            #print(M)
        
        p= identidad(a)

        p[n][n]= (1/M[n][n])

        normalizar_list.append(p)
        
        M= multiplicacion_matrices(p, M)
        #print(M)

        b= identidad(a)
        c= columna(M, n)
        
        for j in range(0, a):
            b[j][n]=-c[j]
            
        b[n][n] = 1
        resta_list.append(b)
        
        M= multiplicacion_matrices(b, M)
        #print(M)
    

    inversa= identidad(a)
    for k in range (0, len(i_list)):
        inversa= multiplicacion_matrices(inversa, i_list[k])
        
    normalizar_list.reverse()
    resta_list.reverse()
    
    for j in range(len (normalizar_list)):
        inversa= multiplicacion_matrices(inversa, resta_list[j])
        #print(inversa)
        
        inversa= multiplicacion_matrices(inversa, normalizar_list[j])
        #print(inversa)    
    return inversa

    
    

#inversa([[0,0,12,2],[1,2,2,1],[12,0,0,1],[1,2,1,0]])
#%% Ejecicio 7 a

if __name__ == '__main__':
    a = matriz_traspuesta(np.array([[1,2,3],[2,3,2],[8,2,3]]))
    b = matriz_traspuesta(a)  
     
    print(f'Matriz Traspuesta: {a}')
    print(f'Matriz Traspuesta a la Traspuesta: {b}')
    
#%% Ejercicio 7b

A= np.array([[1,2,3],[2,3,2],[8,2,3]])
B= np.array([[2,1,2],[2,2,2],[0,1,0]])

resultado = matriz_traspuesta(multiplicacion_matrices(A, B))
resultado

resultado2= multiplicacion_matrices(matriz_traspuesta(B), matriz_traspuesta(A))
resultado2    

#%% Ejercicio 7g    

A= np.array([[1,2,3],[2,3,2],[8,2,3]])
B= np.array([[2,5,2],[1,1,1],[1,1,3]])

c= multiplicacion_matrices(A, B)
c

resultado = inversa(c)
resultado

resultado2= multiplicacion_matrices(inversa(B), inversa(A))
resultado2    

#%% Ejercicio 8
a= 1
b= 2
c= 3    
    
A= [[1,1,38],[0,1,3],[0,0,1]]
inversa(A)

print("\n donde se encuentra a se pone -a,\n donde se encuentra c se pone -c, \n donde se encuentra b se pone -b+c")    
    
#%% Ejercicio 9

A= np.array([[2,1,1],[1,2,1],[1,1,2]])
B=[[2,-1,-1],[-1,2,-1],[-1,-1,2]]
C= np.array([[1,0,0],[2,1,3],[0,0,1]])
D= np.array([[1,1,1],[1,2,2],[1,2,3]])    

inversa(A)
det(B) #no inversible
inversa(C)
inversa(D)

#%% EJERCICIO 10

A= np.array([[1,-1,1,-1],[0,1,-1,1],[0,0,1,-1],[0,0,0,1]])
c=inversa(A)


resultado = multiplicacion_matrices(c, [[1],[1],[1],[1]])
resultado

B= np.array([[1,-1,1,-1,1],[0,1,-1,1,-1],[0,0,1,-1,1],[0,0,0,1,-1],[0,0,0,0,1]])
d=inversa(B)

resultado2 =  multiplicacion_matrices(d, [[1],[1],[1],[1],[1]])
resultado2

#%%
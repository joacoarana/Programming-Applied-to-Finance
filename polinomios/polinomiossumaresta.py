# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 15:15:31 2022

@author: rjara
"""

def suma_polinomios (poli_1,poli_2):
    import numpy as np
    
    p1 = poli_1
    p2 = poli_2
    
    if len (p1)> len (p2):
        p2= [0]*(len(p1)-len(p2)) + p2
        
    elif len (p1)< len (p2):
        p1= [0]*(len(p2)-len(p1)) + p1 
    
    nuevo_polinomio= np.array(p1) + np.array(p2)
    return list(nuevo_polinomio)



def resta_polinomios (poli_1,poli_2):
    import numpy as np
    
    p1 = poli_1
    p2 = poli_2
    
    if len (p1)> len (p2):
        p2= [0]*(len(p1)-len(p2)) + p2
        
    elif len (p1)< len (p2):
        p1= [0]*(len(p2)-len(p1)) + p1 
    
    nuevo_polinomio= np.array(p1) - np.array(p2)
    return list(nuevo_polinomio)



def multiply (poli_1,poli_2):
    
    import numpy as np
    
    p1 = poli_1
    p2 = poli_2
    nuevo_poli = []
    
    if len (p1)> len (p2):
        p2= [0]*(len(p1)-len(p2)) + p2
        
    elif len (p1)< len (p2):
        p1= [0]*(len(p2)-len(p1)) + p1    
    
    for i in range (0, len(p1)):
        lista = []
        
        for n in range (0, len( p2)):
            
            o= p1[i] * p2[n]
            
            lista.append(o)
            #print(lista)
        
        ext= [0] * (len(p2)-i-1)
        
        lista.extend(ext)#cantidad de 0= len(poli2)-i-1
        
        al_principio_0 = [0] * (i)#cantidad de 0= i
                   
        q=  al_principio_0 + lista
        
        nuevo_poli= nuevo_poli + q
        
        nuevo_poli = np.array(nuevo_poli)
        
    nuevo_poli= list(nuevo_poli)    
    
    #print(nuevo_poli) 
    while len(nuevo_poli)>1 and nuevo_poli[0]==0:
            nuevo_poli.pop(0)
        
    return nuevo_poli


            
#multiply ([0], [4,0,3,0])        


def division (dividendo, divisor):
    
    p1= dividendo
    p2= divisor
    
    nuevo_grado =(len(p1)-len(p2))
    
    k=0
    coefs_nuevos= []
    
    while k <= len(p1):
        
        a= p1[0]/p2[0]
        coefs_nuevos.append(a)
        
        b= [0]* nuevo_grado
        b.insert(k, a)
        
        #print(b)
        
        c= multiply(p2, b)
        
        #print(c)
        
        p1= resta_polinomios(p1,c)
        p1.pop(0)
        
        #print(p1)
        
        k= k+1
        
    resto= p1
    
    print (f'el resultado es {coefs_nuevos} y el resto es {resto}')
    return coefs_nuevos

division([5,0,0,3,0,2,1], [4,0,3,0])
















#%%        
        if i == 0:
            lista1 = lista 
            ext= [0] * (len(poli2)-i-1)
            
            lista1.extend(ext)#cantidad de 0= len(poli2)-i-1
            
            al_principio_0 = [0] * (i)#cantidad de 0= i
                       
            a=  al_principio_0 + lista1
            
        elif i ==1:
            lista2 = lista
            ext= [0] * (len(poli2)-i-1)
            
            lista2.extend(ext) #cantidad de 0= len(poli2)-i-1
            
            al_principio_0 = [0] * (i) #cantidad de 0=i
            
            b= al_principio_0 + lista2 # [0] + [6, 10, 14, 0] = [0, 6, 10, 14, 0]
            
        elif i==2:
            
            lista3 = lista  #lista.extend[] #cantidad de 0= len(poli2)-i-1# en este caso nada
            
            ext = [0] * (len(poli2)-i-1)
            
            lista3.extend(ext)
            
            al_principio_0 = [0] * (i)#cantidad de 0= i
            
            c= al_principio_0 + lista3    
            
        elif i==3:
             
             lista4 = lista  #lista.extend[] #cantidad de 0= len(poli2)-i-1# en este caso nada
             
             ext = [0] * (len(poli2)-i-1)
             
             lista4.extend(ext)
             
             al_principio_0 = [0] * (i)#cantidad de 0= i
             
             d= al_principio_0 + lista4
             
    #print(a)
    #print(b)
    #print(c)
    #print(d)

            
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)
    
    producto = a+b+c+d
    return list(producto)


multiply([1,2,3,4], [3,5,7,9])


def ruffini (poli1, raiz):
   
    poli1_menor_grado = []
    resto = []
    a=0
    
    for n in range (0, len(poli1)):
        
        nc= poli1[n] + a
        
        if n != len(poli1)-1:
            poli1_menor_grado.append(nc)
            
        elif n== len(poli1)-1:
            resto.append(nc)
        
        a= nc * raiz
        
    print(f"El polinomio de grado rebajado es {poli1_menor_grado} y el resto es {resto}")
    
    return poli1_menor_grado

ruffini([1,2,-5,-6], -1)
#%%
import numpy as np

poli1 = np.array([1,2,3])
poli2 = np.array([3,5,7])

listanueva =[ poli1[0]*poli2[0]]#x4


listanueva.append([poli1[0]*poli2[1] + poli1[1] * poli2[0]])#x3

listanueva.append([poli1[0]*poli2[2] +poli1[2]*poli2[0] + poli1[1]*poli2[1]]) #x2

listanueva.append(poli1[1]*poli2[2] + poli1[2]*poli2[1]) #x1

listanueva.append(poli1[2]*poli2[2]) #x0

listanueva

#%%
import numpy as np
np.array([1,2,3,4])+ np.array([0,3,2,0])





p = np.polynomial.polynomial.Polynomial([3,-4,1])

s = np.polynomial.polynomial.Polynomial([-1,1,0])

p//s



p= [3,4,1] * 0

p
s= [-1,1,0]

np.polydiv(p, s)

#%%

class cuentas_polinomios():
    
    def __init__(self, poli1, poli2):
        self.poli1 = poli1
        self.poli2 = poli2
    
    def suma_polinomios (self):
        import numpy as np
        
        nuevo_polinomio= np.array(self.poli1) + np.array(self.poli2)
        return list(nuevo_polinomio)

    def resta_polinomios (self):
        import numpy as np
        
        nuevo_polinomio= np.array(self.poli1) - np.array(self.poli2)
        return list(nuevo_polinomio)
    
    def multiply (self):
        
        import numpy as np
        
        p1 = self.poli1
        p2 = self.poli2
        
        for i in range (0, len(self.poli1)):
            lista = []
            
            for n in range (0, len(self.poli2)):
                
                o= p1[i] * p2[n]
                
                lista.append(o)
                #print(lista)
                
            if i == 0:
                lista1 = lista 
                lista1.extend([0,0])#cantidad de 0= len(poli2)-i
                           
                a= lista1
                
            elif i ==1:
                lista2 = lista
                lista.extend([0]) #cantidad de 0= len(poli2)-i
                
                al_principio_0 = [0] #cantidad de 0= len(poli1) -i
                
                b= al_principio_0 + lista2
                
            elif i==2:
                
                lista3 = lista  #lista.extend[] #cantidad de 0= len(poli2)-i# en este caso nada
                
                al_principio_0 = [0,0] #cantidad de 0= len(poli1) -i
                
                c= al_principio_0 + lista3    
        #print(a)
        #print(b)
        #print(c)

                
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        
        producto = a+b+c
        return list(producto)
    
    def ruffini (self, raiz):
       
        poli1_menor_grado = []
        resto = []
        a=0
        coefs = self.poli1
        for n in range (0, len(coefs)):
            
            nc= coefs[n] + a
            
            if n != len(coefs)-1:
                poli1_menor_grado.append(nc)
                
            elif n== len(coefs)-1:
                resto.append(nc)
            
            a= nc * raiz
            
        
        print(f"El polinomio de grado rebajado es {poli1_menor_grado} y el resto es {resto}")
        
        return poli1_menor_grado


    

lol = cuentas_polinomios([1,2,-5,-6], [4,5,6,0])

lol.suma_polinomios()

x=[0,0,0,9]

x[3]+1

len (x)






































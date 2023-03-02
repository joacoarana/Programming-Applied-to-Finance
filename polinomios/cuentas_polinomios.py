# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 20:52:17 2022

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


division([3,2,-8],[1,2])
#%%    


if __name__=='__main__':
        
        a= joaco_poly([1,2,-5,-6])    
        primera_raiz = a.biseccion(0,5)
        print ("La primera raíz encontrada por bisección es:",primera_raiz)
        
        bajar_grado = a.ruffini(2)
        print("El polinomio rebajado por la raiz es:", bajar_grado)
        
        raices_restantes= a.raices_restantes(2, [1,4,3])
        print(f"Todas las raíces del polinomio son :{raices_restantes}")#%%


class polinomicas():
    
    def __init__(self, poli_1, poli_2):
        self.poli_1 = poli_1
        self.poli_2 = poli_2
        
        
    def suma_polinomios (self):
        import numpy as np
        
        p1 = self.poli_1
        p2 = self.poli_2
        
        if len (p1)> len (p2):
            p2= [0]*(len(p1)-len(p2)) + p2
            
        elif len (p1)< len (p2):
            p1= [0]*(len(p2)-len(p1)) + p1 
        
        nuevo_polinomio= np.array(p1) + np.array(p2)
        
        return list(nuevo_polinomio)

    def resta_polinomios (self):
        import numpy as np
        
        p1 = self.poli_1
        p2 = self.poli_2
        
        if len (p1)> len (p2):
            p2= [0]*(len(p1)-len(p2)) + p2
            
        elif len (p1)< len (p2):
            p1= [0]*(len(p2)-len(p1)) + p1 
        
        nuevo_polinomio= np.array(p1) - np.array(p2)
        
        return list(nuevo_polinomio)    


    def multiply (self):
        
        import numpy as np
        
        p1 = self.poli_1
        p2 = self.poli_2
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
            
            c= self.multiply_div(p2, b)
            
            #print(c)
            
            p1= resta_polinomios(p1,c)
            p1.pop(0)
            
            #print(p1)
            
            k= k+1
            
        resto= p1
        
        print (f'el resultado es {coefs_nuevos} y el resto es {resto}')
        return coefs_nuevos

    def multiply_div(self, p2, b):
        
        mult= polinomicas(p2, b)
        
        return mult.multiply()




















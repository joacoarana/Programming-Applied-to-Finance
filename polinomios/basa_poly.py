# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 17:40:14 2022

@author: gbasa
"""
class basa_poly():  
    def __init__(self,parms):
        def f(x):
            y = self.parms[0]
            for i in range(1,len(self.parms)):
                y= self.parms[i] + x*y
            return y
        self.f = f 
        self.parms = parms
    
    def __call__(self,x):
        return self.f(x)    
    
    def fp(self,x,n):  # n es el orden de la derivada
         aux =self.Get_fp(n) 
         y = basa_poly(aux)
         return y(x)
        
    def Get_fp(self,n):
        coefs = self.parms[0:len(self.parms)-n]
        powers = [len(self.parms)-i-1 for i in range(0,len(coefs))]
        salida = coefs
        for i in range(0,len(coefs)):
            salida[i] = coefs[i] 
            for j in range(0,n):
                salida[i]*=powers[i]-j 
        return salida

    def div_monomio(self,x0):  # devuelve divisor p_(n-1) y residuo (que siempre es numero)
        newpol=self.parms
        N = len(newpol)
        salida_= list()
        for i in range(0,N-1):
            salida_.append(newpol[0])
            newpol=[newpol[1]+newpol[0]*x0]+ newpol[2:len(newpol)]

        salida_pol= basa_poly(salida_[0:len(salida_)])
        residuo = newpol[0]
        return salida_pol,residuo 

    def factorize(self,x0):         # cuando x0 es una raiz, devuelve p_(n-1)
        x,y = self.div_monomio(x0)
        return(x)
    
    def Rf_NR(self,x0,nmax=10000, htol_y=0.0000001):
        print('\n *** Buscando raiz para p_n=',self.parms)   
        grado = len(self.parms)-1 # a lo sumo hay grado raices reales
        y0 = self.f(x0)
        yp = self.fp(x0,1)
        
        x1 = x0 - y0/yp
        y1 = self.f(x1)

        if grado>1:
            counter = 0
            while(abs(y1)>htol_y and counter<nmax):
                counter+=1
                x0 = x1
                y0 = y1
                yp = self.fp(x0,1)
                x1 = x0 - y0/yp
                y1 = self.f(x1)
          
            if counter<nmax :
                print('\n Root Found:',x1)
                print('f(x):',self.f(x1))
                print('Polinomio :',self.parms)
                
                newpol = self.factorize(x1)
                salida= [x1]+ newpol.Rf_NR(x1)
            else:
                print('\n Root not found for p_n(x)=',self.parms)
                salida=[]        
        else:
            print('\n Root Found:',x1)
            print('f(x):',self.f(x1))
            print('Polinomio :',self.parms)
            salida = [x1]
        return(salida)            
            
    def Rf_FP(self,x0,nmax=10000, htol_y=0.0000001):
        import numpy as np
        
        def g(x):
            coefs = self.parms
            N = len(coefs)
            aux = basa_poly(-np.array(coefs[1:N])/coefs[0])
            aux2= aux(x)**(1.0/(N-1.0))
            return aux2 
        
        print('\n *** METODO DE PUNTO FIJO') 
        print('      Buscando raiz para p_n=',self.parms)
        print('      Guess: ',x0)
        x = x0
        y = g(x)         
        counter = 1
        while(abs(y-x)>htol_y and counter<nmax):
                counter+=1
                x = y
                y = g(x)
                
        if counter<nmax :
                print('\n Root Found:',x)
                print('f(x):',self.f(x))
                print('Polinomio :',self.parms)
                salida=[x]        
                
                newpol = self.factorize(x)
                print(self.parms)
                print(newpol.parms)
                salida= [x]+ newpol.Rf_FP(x)
        else:
                print('\n Root not found for p_n(x)=',self.parms)
                salida=[]        
        return(salida)            


#%%

if __name__ == '__main__':
    #%%
    aux=[1,2,5]
    x= basa_poly(aux)
    x.Get_fp(2)
    
    #%%
    print('\n\n')     
    
    CF=[-50.0, 10.0, 38.5,41.5,39.5,-80]
    proy=basa_poly(CF)
    x = proy.Rf_NR(1)

    print('\n Raices: \n', x)

    values = [proy.f(xi) for xi in x]
    print('\n Valores: \n',values)







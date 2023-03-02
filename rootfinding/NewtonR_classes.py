# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 20:24:11 2022

@author: gbasa
"""
#%% Definimos una clase de funcion que no tiene derivada analitica

class func_num():
    def __init__(self,f,fprime_a=None,parms=dict(),parmsprime=dict()):
        self.value=f
        self.parms=parms
        self.fprime_a=fprime_a
        self.parmsprime=parmsprime
        
    def __call__(self,x,*args,**kwargs):
        return(self.value(x,self.parms))

    def f_(self,x):
        return self.value(x,self.parms)

    def fp_c(self,x,h=0.0001):
        return  0.5*(self.f_(x+h)-self.f_(x-h))/h   
    
    def fp_f(self,x,h=0.0001):
        return  (self.f_(x+h)-self.f_(x))/h   

    def fp_b(self,x,h=0.0001):
        return  (self.f_(x)-self.f_(x-h))/h   
     
    def fp_a(self,x,h=0.0001):
        if self.fprime_a is None:
            aux = self.fp_c(x,h)
        else:
            aux = self.fprime_a(x)
        return aux
    
    def pltf(self,xmin,xmax,num=100):
        import numpy as np
        import matplotlib.pyplot as plt
        
        x=np.linspace(xmin,xmax,num)
        y=[]
        yp=[]
        for x_i in x:
            y.append(self.f_(x_i))
            yp.append(self.fp_c(x_i))
            
        plt.plot(x,y) 
        plt.plot(x,yp,color='g',linestyle='dotted')
        plt.xlabel('f(x)')
        plt.ylabel('x')
        plt.axhline(color='k',linestyle='dashed')
        plt.show()    
        
#%%
class Rootfinder(func_num):
    def __init__(self, f,fparms=dict()):
        self.f= func_num(f,fparms)
    
    def Search_Guess(self,xmin,xmax,num=100):
        (self.f).pltf(xmin,xmax,num)
    
    def NR(self,deriv,guess,ytol,xtol, Nmax):    
        sols =[]
        x0   = guess
        f0   = (self.f).value(x0) 
        fp0  = deriv(x0)
        sols.append(x0)
        
        x1 = x0-f0/fp0
        f1 = (self.f).value(x1)
        sols.append(x1)
        counter=0
        
        while(abs(x1-x0)>xtol and abs(f1)>ytol and counter<Nmax):
            counter +=1
            fp1 = deriv(x1)
            
            x0 = x1
            f0 = f1
            fp0 = fp1
            
            x1 = x0-f0/fp0
            f1 = (self.f).value(x1)
            sols.append(x1)
            
        if counter<Nmax:
            print('\n Raiz de f(x)=',x1)
            print('\n f(x*)=',f1)        
        else:
            print('\n No se encontró una raíz de f(x)')
            print('\n Ultimo valor de iteracion =',x1)
            print('\n f(x)=',f1)
            
        return(sols)    
    
    def PlotSalida(self,sols):
        import matplotlib.pyplot as plt        
        import numpy as np
        
        x1 = sols[len(sols)-1]	 
        plt.scatter(range(0,len(sols)),sols)        
        plt.xlabel('x_k')
        plt.ylabel('k')
        plt.axhline(y=x1,color='k',linestyle='dashed')
        plt.show()
           
        xmin=min(sols)
        if xmin <0:
           xmin=1.5*xmin
        else:
           xmin=0.5*xmin
           
        xmax=max(sols)
        if xmax >0:
               xmax=1.5*xmax
        else:
               xmax=0.5*xmax
           
        xrange= np.linspace(xmin,xmax,num=100)
        y=[]
        for x_i in xrange:
            y.append((self.f).value(x_i))
               
        plt.plot(xrange,y)
           
        x_s=[]
        y_s=[]
        for x_i in sols:
               x_s.append(x_i)
               y_s.append(0.0)
               x_s.append(x_i)
               y_s.append((self.f).value(x_i))
               
        plt.plot(x_s,y_s,color='g',linestyle='dotted',marker='o')
        plt.xlabel('f(x)')
        plt.ylabel('x')
        plt.axhline(color='k',linestyle='dashed')
        plt.show() 

        
    def FindRoot(self,guess=0,ytol=0.0001, xtol=0.0001, Nmax=1000, Rfparms= dict({'method':'NR','derivada':'c'})) :
        # si se trata de biseccion insertar una tuple
        # para punto fijo, NR o aproximaciones sucesivas,   
        # con un dato alcanza.
        # parms es un diccionario que espefifica 
        #    method (NR,BS,AS o PF)
        #    derivada -- si aplica -- ('f','b','c','a')
        #  si esta vacio, se asume 
        #    method='NR' 
        #    derivada='c'
        
        
        if Rfparms['method']=='AS':
            pass
        elif Rfparms['method']=='BS': 
           pass
        elif Rfparms['method']=='PF':
           pass
        else:                               # por default hace NR
            if Rfparms['derivada']=='b':
                 deriv= (self.f).fp_b 
            elif Rfparms['derivada']=='a':
                deriv= (self.f).fprime_a
            elif Rfparms['derivada']=='f':
                 deriv=(self.f).fp_f
            else: 
                 deriv=(self.f).fp_c       # por default hace 'c'
            sols=self.NR(deriv,guess,ytol,xtol,Nmax)

            self.PlotSalida(sols)
                    

            return(sols)
                                   

#%%  Modularizamos el codigo          
# Se ejecuta esta parte del script solamente
# si  el modulo esta cargado como main program
# dentro del diccionario sys.modules aparece la entrada
# sys.modules['NewtonRclasses']=__main__ 
# Sirve para testear modulos
  
if __name__ == '__main__' :     
# Estas son funciones comunes en formato func_num
    
    def mysin(x,parms=dict()):
        import numpy as np
        return np.sin(x)

    def mycos(x,parms=dict({'frec':2})):
        import numpy as np
        frecuencia = parms['frec']
        return np.cos(frecuencia*x)
    
    def mypol(x,parms=dict({'coefs':[0],'powers':[0]})):
        import numpy as np
        coef= np.array(parms['coefs'])
        pwr = np.array(parms['powers'])
        return np.sum(coef*(x**pwr)) 

    def mypol2(x,parms=[0]):
        aux = parms[0]
        for i in range(1,len(parms)):
            aux +=x*(parms[i]*aux)
        return aux

#myf = func_num(mypol,parms=dict({'coefs':[1],'powers':[3]}))
    myf = func_num(mysin)
    Rf =Rootfinder(myf)
    Rf.Search_Guess(-3.0, 3.0,num=1000)
    Rf.FindRoot(guess=-2.0,Rfparms=dict({'method':'NR','derivada':'c'}))

#%%


def f(x):
    return  (x**2)-4

def biseccion(a,b,tol):
    m1=a
    m=b
    k=0
    
    if f(a)*f(b)>0:
        print ('No tiene raiz')
    
    while(abs(m1-m)>tol):
       m1=m     
       
       m = (a+b)/2
        
       if (f(a)*f(m)<0):
            m=b
            
       if (f(b)*f(m)<0):
            m=a     
               
       print(f"El intervalo es {a}, {b}" )
        
       k= k+1
        
        
    print('x=',k, '=',m, 'es una aproximacion valida')

print(biseccion(-3,-1.5,10**-6))






































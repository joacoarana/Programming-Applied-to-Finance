# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:42:41 2022

@author: rjara
"""
#Clase: auto; entonces una instancia de auto podría ser taxi (taxi = auto) o
# f1 car  = auto

class C1():
    "parent"

class C2(C1):
    "son"
    

issubclass(C2, C1)

#%%

class C1():
    x=10
    def x_se_llama_de_otra_forma_cuando_esta_en_una_funcion(self):
        print(C1.x)

perro = C1()

isinstance(perro, C1)
# self hace referencia a la instancia

#%%

"""_ _init_ _
When a class defines or inherits a method named _ _init_ _, calling the class
object implicitly executes _ _init_ _ on the new instance to perform any needed
instance-specific initialization. Arguments passed in the call must correspond to
the parametersof _ _init_ _, except for parameter self. For example, consider the
following class:
        """

class C6(object):
    
    def  __init__(self, n):
        self.x = n
        
        print (self.x) #self hace referencia a la instancia en cuestión

anotherInstance = C6(42)
secondinstance = C6(21)

print(anotherInstance.x)
        
"""When _ _init_ _ is absent, you must call the class without arguments, and the
newly generated instance has no instance-specific attributes."""        
        
#%%

class Special():
    
    def amethod(self):
        
        print ("special")
        
class Normal():
    
    def amethod(self):
        
        print ("normal")
        
def appropriateCase(x):
    
    if x=="normalito":
        return Normal()
        
    else:
        return Special()

aninstance = appropriateCase("normalito")
aninstance.amethod()        

#%%

def f(a,b):
    
    return a*b
    
class C():
    def __init__(self,a,b):
        
        self.name=f(a, b)

x=C(7,2)
x.name

        
        
        
        
        
        
        
        
        
        
        
        
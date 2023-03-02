#Funciones de Integrales 
#%% 
#Función de prueba:
def f(x):
    return 2*x
#%%
#Método de Trapecios
#sin utilizar vectores (paquete numpy)
def Int_Trapecios(f,x_min,x_max,N=1000):
    intervalos = (x_max-x_min)/N
    suma = 0
    for k in range(1,N):
        region = x_min + k*intervalos
        suma += f(region)
    valor = intervalos *(0.5*f(x_min) + suma + 0.5*f(x_max))
    return valor


#utilizando vectores (paquete numpy)
import numpy as np
#usando linspace de numpy no necesito utilizar for:
def Int_Trapecios2(f,x_min,x_max,N=1000):
    intervalo = (x_max-x_min)/N
    x = np.linspace(x_min,x_max,N+1)
    valor = sum(f(x)) -0.5*f(x_min)-0.5*f(x_max) 
    integral= intervalo*valor
    return integral
#%%
#Método de Riemman

#sin usar vectores
def Int_Riemman(f,x_min,x_max,N=1000):
    intervalo = (x_max-x_min)/N
    suma = 0
    for k in range(0,N):
        region = (x_min + intervalo/2) + k*intervalo
        suma += f(region)
    valor = intervalo*suma
    return valor

#usando linspace de numpy no necesito utilizar for:
    
def Int_Riemman2(f,x_min,x_max,N=1000):
    intervalo = (x_max-x_min)/N
    region = np.linspace(x_min + intervalo/2, x_max-intervalo/2,N)
    valor = intervalo*sum(f(region))
    return valor
    
#%%
#Podemos integrarlas todas en una clase


class Integral():
    def __init__(self,f):
        self.f=f
    
    def Riemman(self,x_min,x_max,N=1000):
        intervalo = (x_max-x_min)/N
        suma = 0
        for k in range(0,N):
            region = (x_min + intervalo/2) + k*intervalo
            suma += f(region)
        valor = intervalo*suma
        return valor
    def Trapecios(self,x_min,x_max,N=1000):
        intervalos = (x_max-x_min)/N
        suma = 0
        for k in range(1,N):
            region = x_min + k*intervalos
            suma += f(region)
        valor = intervalos *(0.5*f(x_min) + suma + 0.5*f(x_max))
        return valor

#%%
#Punto 1 del tp

import numpy as np
            
class Normal():
    def __init__(self,mu,sigma):
        self.mu = mu 
        self.sigma = sigma
        self.a = self.mu - 5*self.sigma
        self.b = self.mu + 5*self.sigma
    def f(self,x):
        return (1/((2*np.pi*(self.sigma**2))**(0.5)) ) *np.exp( -.5 * (((x-self.mu)/self.sigma)**2) )
    
    def int_aux(self,x):
        return self.f(x)
    
    def integrar(self, c, d):
        return Int_Riemman2(self.int_aux,c, d)
    
    def Esp_aux(self,x):
        return x*self.f(x)
    def Var_aux(self,x):
        return ((x-self.mu)**2) * self.f(x)

    def S_aux(self,x):
        return (((x-self.mu)/(self.sigma))**3) * self.f(x)
                
    def K_aux(self,x):
        return (((x-self.mu)/(self.sigma))**4 )*self.f(x)
    
    def Esp(self):
        resultado = Int_Riemman2(self.Esp_aux,self.a,self.b)
        return resultado
    def Var(self):
        return Int_Riemman2(self.Var_aux,self.a,self.b)
    def S(self):
        return Int_Riemman2(self.S_aux,self.a,self.b)
    def K(self):
        return Int_Riemman2(self.K_aux,self.a,self.b)


a= Normal(0, 2)
b= a.integrar(0, 2)
b

prueb1 = Normal(2,1)
# la tabla haganla ustedes 

#%%
#Función Gamma. Usa una clase adentro y crea una instancia de esa clase para utilizar 
#la densidad y su integración en una sola función 
def gamma(n): 
  class Gamma():
    def __init__(self,n):
        self.n=n
    def aux(self,x):
        return (x**(self.n-1))*np.exp(-x)
    def value(self):
        return Int_Riemman2(self.aux,0,20)
  f = Gamma(n)
  return f.value()
#Calculamos la función gamma evaluado en [1,2,3,4,5]
print("Gamma(1) = ",gamma(1))
print("Gamma(2) = ",gamma(2))
print("Gamma(3) = ",gamma(3))
print("Gamma(4) = ",gamma(4))
print("Gamma(5) = ",gamma(5))

#2
rango = list(range(1,11))
resultados1 = list()
for i in rango:
    resultados1.append(gamma(i))
resultados2=list()
for k in rango[:len(rango)-1]:
    resultados2.append(gamma(k))

resultados1 = list(np.array(resultados1)*np.array(rango))
print(resultados1)
print(resultados2)

def factorial(n):
    aux = np.array(list(range(1,n+1)))
    return aux.cumprod()[len(aux)-1]

#probamos para 1,2,3
gamma(3)
factorial(2)
gamma(4)
factorial(3)
gamma(5)
factorial(4)
gamma(6)
factorial(5)



#Para el 3 van a tener que jugar con el limite de integracion
gamma(0.5)
np.pi**(1/2)

#%%

import matplotlib.pyplot as plt
import pandas as pd
class Beta():
    def __init__(self,a,b):
        self.a=a
        self.b=b
        self.beta = self.B()
        self.Esp = self.Esp_f()
        self.Var = self.Var_f()
        self.asimetria = self.S_f()
        self.curtosis= self.K_f()
    def B_aux(self,x):
        return x**(self.a-1)* ((1-x)**(self.b-1))
    def B(self):
        return Int_Riemman(self.B_aux, 0, 1)
    def B_f(self,x):
        if x>=0 and x<=1:
            return  (1/self.beta) * (x**(self.a-1)) * (1-x)**(self.b-1)
        else:
            return 0 
    def density_check(self):
        return Int_Riemman(self.B_f,0,1)
    
    def dist_acum(self,x0,x1):
        return Int_Riemman(self.B_f,x0,x1)
    
    def Esp_aux(self,x):
        return self.B_f(x)*x
    
    def Esp_f(self):
        return Int_Riemman(self.Esp_aux,0,1)
    
    def Var_aux(self,x):
        return ((x-self.Esp)**2)*self.B_f(x)
    
    def Var_f(self):
        return Int_Riemman(self.Var_aux,0,1)
    
    def S_aux(self,x):
        return (((x-self.Esp)/(self.Var))**3) * self.B_f(x)
                
    def K_aux(self,x):
        return (((x-self.Esp)/(self.Var))**4 )*self.B_f(x)
    
    def S_f(self):
        return Int_Riemman(self.S_aux,0,1)
    def K_f(self):
        return Int_Riemman(self.K_aux,0,1)
    
    def plot_density(self):
        rango = np.linspace(-0.5,1.5,1000+1)
        density = list()
        for k in rango:
            density.append(self.B_f(k))
        density = pd.DataFrame(density,index=rango)
        plt.plot(density)
        plt.legend(["Densidad"])
        plt.xlabel("x")
        plt.ylabel("Beta Density")
        title = "Beta Distribution : a = " + str(self.a) + "; b= "+str(self.b)
        plt.title(title)
        plt.grid()


# para a=b=1
ej1 = Beta(1,1)
ej1.plot_density()

ej2=Beta(0.5,0.5)
ej2.plot_density()

#2
#Ya está construida en la clase Beta
#Al inicializar Beta(a,b).beta obtenemos el resultado que queremos 

def verificacion(a,b):
    beta_aux = Beta(a,b)
    v_beta = beta_aux.beta
    v_gamma = (gamma(a)*gamma(b))/(gamma(a+b))
    return v_beta,v_gamma

#3:
beta = Beta(1,1)
beta.plot_density()
beta.dist_acum(0,0.5)    #los argumentos de entrada son la región de integración x0--x1
beta.Esp  #ya está la rutina
beta.Var
var_formula=(beta.a*beta.b) / (((beta.a+beta.b)**2)*(1+beta.a+beta.b)   )
beta.curtosis #method que calcula coeficiente de curtosis
beta.asimetria #method que calcula coeficiente de asimetria




#%%
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class Activo():
    def __init__(self,ticker,period,interval):
        self.ticker = ticker
        self.period=period
        self.interval = interval
        self.returns = self.returns()
        self.rets = list(self.returns["Returns"])
        self.n = len(self.returns)
        self.media = self.media()
        self.var = self.var()
        self.sigma = self.var**(1/2)
        self.s=self.s()
        self.k=self.k()
    def returns(self):
        activo = yf.download(self.ticker,period=self.period,interval=self.interval)["Adj Close"].dropna(how="all")
        n = len(activo)
        rets =np.array([0])
        for i in range(n-1):
            rets = np.append(rets,( activo[i+1]/activo[i])-1)
        returns = pd.DataFrame({"Returns":rets},index=activo.index)
        return returns
    def plot_returns(self):
      plt.plot(self.returns,color="crimson")
      title = str(self.ticker)+ ": Historical Returns"
      plt.title(title)
      plt.style.use('dark_background')
      plt.xlabel("Year")
      plt.grid()
      plt.ylabel("%")
    def media(self):
        return float(sum(self.rets)/self.n)
    def var(self):
        return float(sum (((np.array(self.rets) - self.media)**2))/self.n)
    def s(self):
        return float(sum( ((np.array(self.returns)-self.media)**3)) /(self.n*(self.sigma**3)))
    def k(self):
        return float(sum ( ((np.array(self.returns)-self.media)**4)) /(self.n*(self.sigma**4)))
    
n * ()

    
MSFT = Activo("MSFT","15y","1wk")
MSFT.returns
MSFT.plot_returns()
MSFT.k
MSFT.media
MSFT.var
MSFT.s


# Importamos todos los modulos necesarios.
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use("seaborn")

#%%

#Método de Trapecios
# Sin utilizar vectores (paquete numpy)

def Int_Trapecios(f,x_min,x_max,N=1000):
    intervalos = (x_max-x_min)/N
    suma = 0
    for k in range(1,N):
        region = x_min + k*intervalos
        suma += f(region)
    valor = intervalos *(0.5*f(x_min) + suma + 0.5*f(x_max))
    return valor

# Utilizando vectores (paquete numpy)


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
            suma += self.f(region)
        valor = intervalo*suma
        return valor
    def Trapecios(self,x_min,x_max,N=1000):
        intervalos = (x_max-x_min)/N
        suma = 0
        for k in range(1,N):
            region = x_min + k*intervalos
            suma += self.f(region)
        valor = intervalos *(0.5*self.f(x_min) + suma + 0.5*self.f(x_max))
        return valor

#%%

# Punto 1 del tp
# Clase distribucion normal
         
class Normal():
    def __init__(self,mu,sigma):
        # Mu = promedio de los retornos
        # Sigma = desvio estandar de los retornos --> raiz de la varianza
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
    def plot_density(self):
        x = np.linspace(-10, 10, 1000)
        y = [self.f(i) for i in x]
        plt.figure()
        plt.title(f"Funcion de densidad de la normal; mu = {self.mu}, sigma = {self.sigma}")
        plt.plot(x, y, linewidth = 1, color = "black")
        plt.show()
    

#n= Normal(0, 1)
#n.plot_density()
 
#%%

# Función Gamma. Usa una clase adentro y crea una instancia de esa clase para utilizar.
# La densidad y su integración en una sola función.

def gamma(n): 
  class Gamma():
    def __init__(self,n):
        self.n=n
    def aux(self,x):
        return (x**(self.n-1))*np.exp(-x)
    def value(self):
        return Int_Riemman2(self.aux, 0, 17, 1000000)
  f = Gamma(n)
  return f.value()

#%%

#gamma(2)

#%%

# Clase de distribucion Beta

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
        plt.grid()
        plt.legend(["Densidad"])
        plt.xlabel("x")
        plt.ylabel("Beta Density")
        title = "Beta Distribution : a = " + str(self.a) + "; b= "+str(self.b)
        plt.title(title)
        plt.grid()
        
#%%        
#b= Beta(0, 1)
#b.plot_density()

#%%

class Activo():
    
    def __init__(self,ticker,period,interval):
        self.ticker = ticker
        self.period = period
        self.interval = interval
        self.returns = self.returns()
        self.rets = list(self.returns["Returns"])
        self.n = len(self.returns)
        self.sigma = self.var(False) ** 0.5
   
    def returns(self):
        activo = yf.download(self.ticker,period=self.period,interval=self.interval)["Adj Close"].dropna(how="all")
        n = len(activo)
        rets = np.array([0])
        for i in range(n-1):
            rets = np.append(rets,( activo[i+1]/activo[i])-1)
        returns = pd.DataFrame({"Returns":rets},index=activo.index)
        return returns
    
    def prices(self):
        activo = yf.download(self.ticker,period=self.period,interval=self.interval)["Adj Close"].dropna(how="all")
        return activo
    
    def plot_price(self, intervalo = 20):
        prices = list(self.prices())
        dias = list(self.prices().index)
        mm = self.media_movil(intervalo)
        plt.figure()
        plt.grid()
        plt.plot(dias, prices)
        plt.plot(dias[intervalo-1:], mm, "red", linewidth = 0.75)
        plt.xlabel("Year")
        plt.ylabel("Price U$D")
        plt.title(f"Grafico: {self.ticker}")
        plt.legend(["Price", "Media movil"])
        plt.grid()
        plt.show()
    
    def plot_returns(self):
        plt.grid()
        returns = list(self.returns.Returns)
        returns = [i*100 for i in returns]        
        plt.plot(list(self.returns.index), returns)
        title = str(self.ticker)+ ": Historical Returns"
        plt.title(title)
        plt.style.use('seaborn')
        plt.xlabel("Year")
        plt.grid()
        plt.ylabel("%")
        
    def diagrama_dispersion(self):
        plt.grid()
        returns = list(self.returns.Returns)
        returns = [i*100 for i in returns]
        plt.scatter(list(self.returns.index), returns, s = 10)
        title = f"Diagrama de Dispersion: {self.ticker}"
        plt.title(title)
        plt.style.use('seaborn')
        plt.xlabel("Year")
        plt.grid()
        plt.ylabel("%")
                
    def plot_ewma(self, lmbda = 0.8):
        plt.grid()
        returns = list(self.returns.Returns)
        plt.plot(list(self.returns.index), returns, "blue")
        ewma = [i**0.5 for i in self.EWMA(lmbda)[1:]]
        plt.plot(list(self.returns.index), ewma, "red")
        title = str(self.ticker)+ ": Returns + EWMA Model"
        plt.title(title)
        plt.style.use('seaborn')
        plt.xlabel("Year")
        plt.legend(["Returns", "EWMA Model"])
        plt.grid()
        plt.show()
        
    def media_movil(self,dias):
        precios = list(self.prices())
        media = []
        for i in range (dias,self.n+1):
            media.append(np.mean(precios[i-dias:i]))
        return media
       
    def media(self):
        media = float(sum(self.rets)/self.n)
        # print(f"\n{self.ticker} media: {media}")
        return media
    
    def var(self, p = True):
        var = float(sum (((np.array(self.rets) - self.media())**2)) / self.n)
        if p:
            print(f"\n{self.ticker} varianza: {var}")
        return var
    
    def s(self):
        s = float(sum(((np.array(self.returns)-self.media())**3)) / (self.n*(self.sigma**3)))
        print(f"\n{self.ticker} coeficiente de asimetria: {s}")
        return s
    
    def k(self):
        k = float(sum(((np.array(self.returns)-self.media())**4)) / (self.n*(self.sigma**4)))
        print(f"\n{self.ticker} kurtosis: {k}")
        return k
    
    def k_exceso(self):
        k = self.k - 3
        print(f"\n{self.ticker} exceso de kurtosis: {k}\n")
        return k
    
    def desv_estandar(self):
        # Desvio estandar muestral.
        desv = list()
        for i in self.returns:
            desv.append((i-self.media())**2)
        desvio = (sum(desv)/self.n)**0.5
        print(f"\n{self.ticker} desvio estandar muestral: {desvio}")
        return desvio
    
    def EDP(self, printout = True):
        edp = ((self.n-2)/6)*((self.s**2 + (self.k_exceso**2)/4))
        print(f"\n{self.ticker} estadistico de prueba: {edp}")
        return edp
    
    def EWMA(self, lmbda = 0.8):
        ewma_list = [0]
        returns = list(self.returns.Returns)
        for i in range(len(self.returns)):
            varn = lmbda * ewma_list[i] + (1-lmbda)*(returns[i]**2)
            ewma_list.append(varn)
        return ewma_list
#%%
# Apple = Activo("AAPL", "10y", "1wk")
# Apple.plot_price(10)
# Apple.plot_returns()

#%% 

def covarianza(xi, yi):
    import numpy as np
    x_, y_ = np.mean(xi), np.mean(yi)
    N = len(xi)
    suma = 0
    for i in range(N):
        suma += (xi[i] - x_)*(yi[i] - y_)
    covarianza = suma/N
    return covarianza

def coef_correlacion(xi, yi):
    retornosxi = list(xi.returns.Returns)
    retornosyi = list(yi.returns.Returns)
    covxy = covarianza(retornosxi, retornosyi)
    desvxi = xi.sigma
    desvyi = yi.sigma
    return covxy/(desvxi*desvyi)
        
#%%

class t_student():
    # La media de un t student es siempre cero. 
    # La media esta centrada en cero. T student es una aproximacion con muestra pequeña de la normal (0,1).
    def __init__(self, n):
        self.n = n
        self.mu = self.Esp()
        self.sigma = (self.Var())**0.5
    
    def f(self, x):
        # Funcion de densidad de t-student
        import numpy as np
        gamma1 = gamma((self.n + 1)/2)
        gamma2 = gamma(self.n/2)
        sec = (1+(x**2)/self.n) ** -((self.n + 1) / 2)
        fx = (1/(self.n * np.pi)**0.5) * (gamma1/gamma2) * sec
        return fx
        
    def int_f(self):
        return Int_Riemman(self.f, -10, 10)

    def plot(self):
        import matplotlib.pyplot as plt
        import numpy as np
        plt.figure()
        plt.grid()
        plt.title("T-Student Distribution")
        x = np.linspace(-10, 10, 100)
        y = [self.f(i) for i in x]
        plt.plot(x,y)
        plt.grid()
        plt.show()
        
    def Esp_aux(self,x):
        return x*self.f(x)
   
    def Var_aux(self,x):
        return (x**2) * self.f(x)

    def S_aux(self,x):
        return (((x)/(self.sigma))**3) * self.f(x)
                
    def K_aux(self,x):
        return (((x)/(self.sigma))**4 )*self.f(x)
    
    def Esp(self):
        resultado = Int_Riemman2(self.Esp_aux, -10, 10)
        return resultado
    
    def Var(self):
        return Int_Riemman2(self.Var_aux, -12, 12)
   
    def S(self):
        return Int_Riemman2(self.S_aux, -12, 12)
    
    def K(self):
        return Int_Riemman2(self.K_aux, -10, 10) # para exceso de kurtosis: - 3
#%%
#a= t_student(8)
#a.plot()
#a.Var()





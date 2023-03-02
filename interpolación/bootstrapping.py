# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 23:35:55 2022

@author: rjara
"""

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


xi= [1, 2, 3, 6, 12,24,36,60,84,120,240,360]
yi=[0.00634, 0.008833, 0.0101635, 0.014756, 0.0204955, 0.025848, 0.027335, 0.0280515, 0.0282115, 0.027874, 0.031766, 0.029924]

a= xy(xi, yi)
b= a.get_spot_curve()






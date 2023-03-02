# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:41:10 2022

@author: rjara
"""

number = int(input("Number:"))

for n in range(1,number):
    
    if number % n == 0:
        
        print(f"{n} is a factor of {number}")
        
    else:
        
        print(f"{n} is not a factor of {number}")


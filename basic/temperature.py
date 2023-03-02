# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 19:43:48 2022

@author: rjara
"""

def convert_to_Cel(c):
    result = round((int(c)*(1.8)+32),2)
    return result
print(convert_to_Cel(input()))

def convert_to_F(f):
    result = round((int(f)-32)*(5/9),2)
    return result
print(convert_to_F(input()))
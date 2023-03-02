# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 10:57:21 2022


"""
total = 0

def add_to_total(n):
    
    global total
    
    total = total+n

    return total


add_to_total(5)


print(total)
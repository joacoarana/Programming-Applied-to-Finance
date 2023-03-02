# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:24:22 2022

@author: rjara
"""

import random

print(random.randint(1,10))

#%%
#joaco

    
heads = 0

tails = 0

for n in (1, 10000):
    
    coin= random.randint(0,1)
    
    if coin == 1:
            tails = tails + 1
    
    else:
            heads = heads + 1
        
            print= (heads)
        
#%%

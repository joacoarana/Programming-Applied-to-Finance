# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 20:00:37 2022

@author: rjara
"""

sum_of_evens = 0

for n in range(1, 100):
    
    if n % 2 == 0:
        
        sum_of_evens = sum_of_evens + n


print(sum_of_evens)

#%%

for n in range(0, 4):
    
    
    print(n)
    
    if n == 2:
        
        break
    
#%%

for n in range(0, 4):
    
    if n == 2:
        break
    print(n)
        
print(f"Finished with n = {n}")

#%%

for i in range(0, 4):
    
    if i == 2:
        continue
    
    print(i)
    
print(f"Finished with i = {i}")

#%%

for n in range(3):
    
    password = input("Password: ")
    
    if password == "12345":
        break
    
    print("Password is incorrect.")
    
else:
    print("Suspicious activity. The authorities have been alerted.")

#%%

try:
    number = int(input("Enter an integer: "))
    
except ValueError:
    print("That was not an integer")

#%%
try:
    ("lol")
except :
    print("Somethg bad happened")
    
#%%











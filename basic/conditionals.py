# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 19:10:25 2022

@author: rjara
"""

if 2 + 2 == 4:
    print("2 and 2 is 4")
    
#%%

if 2 + 2 == 5:
    print("Is this the mirror universe?")
    
#%%

Boca = (2)

if Boca <=1:
    
    print("DALE BOOOOO")
    
else:
    print("ESTAMOS EN LA B")

#%%

grade = 69

if grade >= 70:
    print("You passed the class!")
    
else:
    print ("No pasaste mi rey")
 #%%
 
grade = int(input("grade")) # 1
 
if grade >= 90: # 2

    print("You passed the class with a A.")
    
elif grade >= 80: # 3


    print("You passed the class with a B.")


elif grade >= 70: # 4

    print("You passed the class with a C.")
    
else: # 5
    print("You did not pass the class :(")
    
    
print("Thanks for attending.") 
 #%%
 
sport = input("Enter a sport: ")
 
p1_score = int(input("Enter player 1 score: "))

p2_score = int(input("Enter player 2 score: "))

# 1
if sport == "basketball":
    
    if p1_score == p2_score:
        print("The game is a draw.")
        
    elif p1_score > p2_score:
        print("Player 1 wins.")

    else:
        print("Player 2 wins.")
        
# 2
elif sport == "golf":
    
    if p1_score == p2_score:
        print("The game is a draw.")
        
    elif p1_score < p2_score:
        print("Player 1 wins.")
        
    else:
        print("Player 2 wins.")
# 3
else:
    print("Unknown sport")
    
#%%
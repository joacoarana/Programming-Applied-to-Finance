# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 21:46:23 2022

@author: rjara
"""

cashflow = (1,2,3,34) #no puede ser tuple (1,2,3,34) , eso solo para strings


type (cashflow)

#%%

tuple ("23445W")

#%%

Tuplee = (1,3,4,5,9,0)

len (Tuplee)

Tuplee [4]

Tuplee[2:5]

Tuplee[2] ==4

9 in Tuplee
#%%

cardinal_numbers= ("first", "second", "third")

position1 = cardinal_numbers[0]
position2 = cardinal_numbers[1]
position3 = cardinal_numbers[2]

print(position1, position2, position3)

for value in cardinal_numbers:
    print(value)

#%%

colors = ["red", "yellow", "green", "blue"]
type(colors)

#%%

tuple1= (1,2,3)

list(tuple1)
#%%

#Tuplee.split() #separator

groceries = "eggs, milk, cheese"
grocery_list = groceries.split(", ")
grocery_list

#%%

# Split string on multiple characters
"abbaabba".split("ba") #ba es separador


#%%

#cambiar elemento de una lista

colors = ["red", "yellow", "green", "blue"]
colors[0] = "burgundy"

colors

colors[1:3] = ["orange", "magenta"]

colors

#%%


colors = ["red", "yellow", "green", "blue"]

# Insert "orange" into the second position (list.insert())

colors.insert(1, "orange")

colors

colors.insert(10, "orange1")

colors[5]

##%% -1 es el ultimo numero de la lista

color = colors.pop()

color
'green'
colors

#%%

colors.append("indigo") #Se agrega a lo último de la fila


colors.extend(("violet", "ultraviolet"))


colors

#%%

nums = [1, 2, 3, 4, 5]

nums.insert(0,0)

nums

total = 0

for number in nums:
    total = total + number

total

#or

sum(nums)

#or

sum([1, 2, 3, 4, 5])

min(nums)

max(nums)

#%%

#List comprehension: List comprehensions are commonly used to convert 
#values into a different type

numbers = (1, 2, 3, 4, 5)

squares = [num**2 for num in numbers]

squares

#%%

#EJERCICIO

breakfast = ("eggs, fruit, orange")

breakfast1 = breakfast.split(",")

breakfast1

type(breakfast1)

lenghts = [len(num) for num in breakfast1]

lenghts

#%%

#Nested List: List as a value in another List or tuple

two_by_two = [[1, 2], [3, 4]]

two_by_two[1][0]

#%%
#Copying

animals = ["lion", "tiger", "frumious Bandersnatch"]

large_cats = animals[:]

large_cats.append("leopard")

large_cats

animals

#%%

#Sorting

colors = ["red", "yellow", "green", "blue"]

colors.sort()

colors

# Lists of numbers are sorted numerically
numbers = [1, 10, 5, 3]

numbers.sort()

numbers

#%%

colors = ["red", "yellow", "green", "blue"]

colors.sort(key=len)

colors

#%%

def get_second_element(item):
    
    return item[1]

items = [(4, 1), (1, 2), (-9, 0)]

items.sort(key=get_second_element)

items





















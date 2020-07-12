# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 19:00:38 2020

@author: ikhurana
"""

#%%
# List compreshension
# Dictionary comprehension

l = [x ** 0.5 for x in range(10)]

a,b,c = (1,2,3)
#%%
# syntax for comprehension

# [end_value for end_value in iterator if <condition>]
[i for i in x if i%2 == 0]
print([str(i)+" is even" if i%2 == 0 else str(i)+" is odd" for i in range(1,100)])

i%2 == 0 

if i%2 == 0:
    "Even"
else:
    "odd"
"even" if i%2 == 0 else "odd"


d = {'name': 'Ishan', 'last_name': 'khurana', 'score': 50}


for  key, value in d.items():
    print(key, " :: ", value)
    
keys = ['name', 'last_name', 'score']
values = ["values", 'Ishan', "random", 'khurana', "random2", 50, ]

d1 = {k:v for k in keys for v in values}

"""
two methods:
1. zip
2. idx checking : enumerate
"""

# 1. zip = zip, compress the values from 2 or more iterables into 1  list
d1 = {k:v for k, v in zip(keys, values)}

# idx checking using enumerate
d2 = {k:v for idx, k in enumerate(keys) for idx2, v in enumerate(values) if idx == idx2}

#%%
"""
functions: named block which take some input, process them and may or may not return an output
# you want to use this block again and again

def <function_name>(<function parameters>):
    <function_body>
    <return <values>>
"""
# write a function which takes a number and print if it is even or odd

 

def even_or_odd(number):
    if number % 2 == 0:
        print(number, " :: even")
    else:
        print(number, " :: odd")
    
    return    
    

for i in range(20):
    even_or_odd(i)

#%%
def even_or_odd2(number):
    for i in range(number):
        even_or_odd2(i)
        # if i % 2 == 0:
        #     print(i, " :: even")
        # else:
        #     print(i, " :: odd")
    return    

even_or_odd2(5)

#%%

def even_or_odd3(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "odd"
    

for i in range(20):
    print(i, ":: ", even_or_odd3(i))

#%%
1. list of strings and for each string you have to find the frequency of each character
2. define a funciton to check if number is prime or not 
3.  fibonacci program using recursion




































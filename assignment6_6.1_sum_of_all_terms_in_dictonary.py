# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:23:14 2020

@author: Administrator
"""


#Write a Python program to sum all the items in a dictionary?
def returnSum(myDict): 
    sum = 0
    for i in myDict: 
        sum = sum + myDict[i] 
    return sum
dict = {'a': 34, 'b':200, 'c':300} 
print("Sum :", returnSum(dict))  
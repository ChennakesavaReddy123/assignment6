# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:49:26 2020

@author: Chennakesava Reddy
"""


#4.Write a python program to add keys/values in a dictionary (update dictionary)?
key=int(input("Enter the key (int) to be added:"))
value=int(input("Enter the value for the key to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)
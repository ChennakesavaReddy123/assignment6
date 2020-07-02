# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:00:50 2020

@author: Chennakesava Reddy
"""

#6.Write a python program to remove items from the dictionary in Python?
thisdict = {
  "brand": "godreg",
  "model": "bang",
  "year": 1947
}
thisdict.pop("model")
print(thisdict)
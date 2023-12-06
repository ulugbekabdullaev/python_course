# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 09:23:17 2023

@author: Ulugbek
"""

def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar


print(fibonacci(10))
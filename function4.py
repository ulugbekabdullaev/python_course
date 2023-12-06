# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:06:26 2023

@author: Ulugbek
"""


def kattasi(x, y, z):
    max = x
    if y >= max:
        max = y
    if z >= max:
        max = z
    return max
katta=kattasi(10,12,18)
print(katta)
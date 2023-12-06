# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 20:56:01 2023

@author: Ulugbek
"""

def sonlar(min, max):
    tub_sonlar=[]
    for n in range (min,max+1):
        tub=True
        if n==1:
            tub=False
        elif n==2:
            tub=True
        else:
            for x in range (2,n):
                if n%x==0:
                    tub=False
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar

print(sonlar(1,100))
        
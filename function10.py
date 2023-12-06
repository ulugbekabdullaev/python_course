# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:43:31 2023

@author: Ulugbek
"""

def kopaytma_hisobla(*sonlar):
    kopaytma=1
    for son in sonlar:
        kopaytma *=son
    return kopaytma

print(kopaytma_hisobla(2,3,4))

def ayirma_hisobla(*sonlar):
    ayirma=0
    for son in sonlar:
        ayirma -=son
    return ayirma

print(ayirma_hisobla(2,3,4))

def bolinma_hisobla(*sonlar):
    bolinma=100
    for son in sonlar:
        bolinma /=son
    return bolinma

print(bolinma_hisobla(2,3,4))
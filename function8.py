# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:17:38 2023

@author: Ulugbek
"""

def katta_harf(matnlar):
    ismlar=[]
    for ism in matnlar:
           ismlar.append(ism.title())
    return ismlar
        
matnlar = ["ali", "vali", "hasan", "husan"]
ismlar=katta_harf(matnlar)
print(matnlar)
print(ismlar)
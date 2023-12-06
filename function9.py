# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 10:34:33 2023

@author: Ulugbek
"""

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism]=baho
    return baholar

ismlar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(ismlar)
print(baholar)
print(ismlar)
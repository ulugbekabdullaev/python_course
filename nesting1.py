# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 21:02:34 2023

@author: Ulugbek
"""

kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }
for ism,kinolar in kinolar.items():
    print(f"\n{ism.title()}ning yaxshi ko'rgan kinolari:")
    for kino in kinolar:
        print(kino)
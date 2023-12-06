# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 13:11:10 2023

@author: Ulugbek
"""

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}
while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        print(f"{buyurtma}-{mahsulotlar[buyurtma]} so'm")
    else: print(f"Bizda {buyurtma} yo'q")
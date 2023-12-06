# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 12:49:30 2023

@author: Ulugbek
"""

buyurtmalar=[]
savol="Buyurmangizni kiriting(to'xtatish uchun 'stop' deb yozing):"
while True:
    buyurtma=input(savol)
    if buyurtma=="stop":
        break
    buyurtmalar.append(buyurtma)
print("Sizning buyurmalaringiz:")
for buyurtma in buyurtmalar:
    print(buyurtma)
    
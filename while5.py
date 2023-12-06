# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 13:03:10 2023

@author: Ulugbek
"""

e_bozor={}
ishora=True
while ishora:
    buyum=input("Buyumning nomini kiriting:")
    narx=input(f"{buyum}ning narxini kiriting:")
    e_bozor[buyum]=int(narx)
    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for buyum, narx in e_bozor.items():
    print(f"{buyum.title()} {narx} so'm")
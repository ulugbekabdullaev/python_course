# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:29:19 2023

@author: Ulugbek
"""

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat=='exit':
        break
    elif float(qiymat)<0:
        print("Manfiy sondan kvadrat ildiz chiqmaydi")
    else:
        ildiz =float(qiymat)**0.5
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
print("Dastur tugadi")
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 13:52:28 2023

@author: Ulugbek
"""

#dictionary={"str":"matn","float":"ixtiyoriy son","int":"butun son","if":"agar","boolean":"mantiqiy qiymat"}
#for key, value in sorted(dictionary.items()):
#    print(f"{key} - {value}")
#davlatlar = {
#    "o'zbekiston":'toshkent',
#    'aqsh':'washington d.c.',
#    'rossiya':'moskva',
#    'tojikiston':'dushanbe',
#    "qirg'iziston":'bishkek',
#    'qozog\'iston':'nursulton',
#    'malayziya':'kuala-lumpur',
#    'singapur':'sungapur',
#    'italiya':'rim'}
#print("Dunyo davlatlari:")
#for davlat in sorted(davlatlar.keys()):
#    print(davlat.title())
#print("Davlatlarning poytaxti:")
#for poytaxt in sorted(davlatlar.values()):
#    print(poytaxt.title())
#country=input("please enter the name of your country:").lower()
#if country in davlatlar.keys():
#    print(f"{country.title()}ning poytaxti {davlatlar[country].title()} shahri")
#else: print("not found")
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }
meals=[]
for n in range(3):
    meals.append(input(f"{n+1}-taom:").lower())
for meal in meals:
    if meal in menu.keys():
        print(f"{meal} {menu[meal]} so'm")
    else: print("Bizda bunday taom mavjud emas")
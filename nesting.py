# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:31:33 2023

@author: Ulugbek
"""

buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'm_asar':'Al Jome As Sahih'
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'm_asar':'Mehrobdan Chayon'
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'm_asar':"O'zbegim"
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'm_asar':"Hamsa"
           }
#shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
#for shaxs in shaxslar:
#    ism = shaxs['ism']
#    tyil = shaxs['tyil']
#    vyil = shaxs['vyil']
#    tjoy = shaxs['tjoy']
#    print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
#         f"{vyil-tyil} yil umr ko'rgan.")
#for shaxs in shaxslar:
#    ism = shaxs['ism']
#    m_asar=shaxs['m_asar']
#    print(f"{ism}ning eng mashhur asari {m_asar}")

kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }
for ism in kinolar.items():
    print(f"\n{ism.title()}ning yaxshi ko'rgan kinolari:")
    for kino in kinolar:
        print(kino)
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:56:49 2023

@author: Ulugbek
"""

#def yosh_hisobla(ism, tugilgan_yil):
#    """Foydalanuvchi yoshini hisoblaydigan dastur"""
#    print(f"{ism.title()} {2023-tugilgan_yil} yoshda")
#yosh_hisobla("Ulugbek", 2002)

#def yosh_hisobla(ism, tugilgan_yil):
#    """Foydalanuvchi yoshini hisoblaydigan dastur"""
#    print(f"{ism.title()} {2023-tugilgan_yil} yoshda")

#ism=input("Ismingizni kiriting:").title()
#tugilgan_yil=int(input("Tug'ilgan yilingizni kiriting:"))
#yosh_hisobla(ism, tugilgan_yil)

#def darajani_hisobla(son):
#    """Sonning kvadrati va kubini hisoblaydigan dastur"""
#    print(f"{son}ning kvadrati {son**2}ga teng\n"
#          f"{son}ning kubi {son**3}ga teng")
#son=float(input("ixtiyoriy sonni kiriting:"))
#darajani_hisobla(son)

#def juftlikka_tekshir(son):
#    """Sonning juft yoki toq ekanligini aniqlaydigan dastur"""
#    if son%2==0:
#        print(f"{son} juft son")
#    else: print(f"{son} toq son")
#son=float(input("ixtiyoriy sonni kiriting:"))
#juftlikka_tekshir(son)

def solishtir(x,y):
    """Ikki sonni solishtiruvchi funksiya"""
    if x>y:
        print(f"{x}>{y}")
    elif x<y:
        print(f"{y}>{x}")
    else:
        print(f"{x}={y}")

solishtir(10,20)
solishtir(-9,12)
solishtir(1223*5,5**4)
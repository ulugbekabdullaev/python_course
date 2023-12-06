# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:30:00 2023

@author: Ulugbek
"""

#def darajani_hisobla(x,y=2):
#    """x ning y-darajasini hisoblaydigan dastur"""
#    print(f"{x}ning {y}-darajasi {x**y}ga teng")

#darajani_hisobla(101)


def bolinish_alomatlari(son):
    for n in range(2,11):
        if son%n==0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(26)
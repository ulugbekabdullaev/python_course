# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 19:10:02 2023

@author: Ulugbek
"""

"Son top o'yini"

print("Keling o'ylagan sonni topishni o'ynaymiz!")


import random
def sontop(x=10):
    son=random.randint(1,x)
    print("Men 1 dan 10 gacha son o'yladim. Topa olasizmi?")
    taxminlar=0
    while True:
        taxminlar +=1
        taxmin=int(input(">>>"))
        if son>taxmin:
            print("Men o'ylagan son bundan kattaroq")
        elif son<taxmin:
            print("Men o'ylagan son bundan kichikroq")
        else:
            break
    print(f"Tabriklaymiz. {taxminlar} ta taxminda topdingiz")
    return taxminlar
print(sontop(x=10))



def sontop_pc(x=10):
    input(print("1 dan 10 gacha son o'ylang va men uni topishga harakat qilaman. Davom ettirish uchun 'enter' tugmani bosing."))
    taxminlar=0
    quyi=1
    yuqori=x
    while True:
        taxminlar +=1
        if quyi!=yuqori:
            taxmin=random.randint(quyi,yuqori)
        else:
            taxmin=quyi
        javob=input(f"Siz {taxmin} ni o'yladingiz. Agar o'ylagan soningiz {taxmin} dan katta bo'lsa '+',"
                    f"kichik bo'lsa '-' {taxmin} 'ok' ni bosing>>>")
        if javob=="+":
            quyi=taxmin+1
        elif javob=="-":
            yuqori=taxmin-1
        else:
            break
    print(f"{taxminlar} ta taxminda topdim!")
    return taxminlar
print(sontop_pc(x=10))



def play(x):
    yana=True
    while yana:
        taxminlar_user=sontop(x)
        taxminlar_pc=sontop_pc(x)
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz!")
        else:
            print("Durrang!")
        yana=int(input("Yana o'ynaysizmi? Ha(1)/Yo'q(0):"))

print(play(x=10))













   
        
    
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 11:17:21 2023

@author: Ulugbek
"""

def malumotlar(ism, familiya,**qoshimcha):
    qoshimcha["ism"]=ism
    qoshimcha["familiya"]=familiya
    return qoshimcha
talaba=malumotlar("ali", "valiyev", t_yili=2002, t_joyi="buxoro")
print(talaba)

def malumotlar(**qoshimcha):
    return qoshimcha
talaba=malumotlar(ism="ali", familiya="valiyev", t_yili=2002, t_joyi="buxoro")
print(talaba)

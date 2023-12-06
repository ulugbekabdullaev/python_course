# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 11:19:44 2023

@author: Ulugbek
"""

#father={"name":"Uygun","age":"43","nationality":"uzbek"}
#mother={"name":"Dilfuza","age":"43","nationality":"uzbek"}
#brother={"name":"Amirbek","age":"10","nationality":"uzbek"}
#(f"My father's name is {father['name']}, his age {father['age']}, his nationality {father['nationality']}")
#meal={"Ilhom":"osh","Ali":"manti","Vali":"kabob"}
#print(f'Alining yoqtirgan taomi {meal["Ali"]}')
dictionary={"str":"matn","float":"ixtiyoriy son","int":"butun son","if":"agar"}
word=input("please enter one of the python variable types:")
if word in dictionary:
    print(dictionary[word])
else: print("not defined")
print(dictionary.get(word, "bunday so'z mavjud emas"))
print(dictionary.get(word))
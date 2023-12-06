# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:41:32 2023

@author: Ulugbek
"""

#names=["Jack", "Michael", "Robert"]
#print("how are you", names[0])
#numbers=[400, 768.2, 49474, 42984]
#numbers[1]=4008
#print(numbers)
#t_shaxslar=["Buxoriy", "Navoiy"]
#z_shaxslar=["Musk", "Bezos"]
#print("Men tarixiy shaxslardan", t_shaxslar.pop(), "bilan\nZamonaviy shaxslardan esa", z_shaxslar.pop(0), "bilan suhbat qilgan bo'lar edim" )
friends=[]
friends.append("Nick")
friends.append("Jack")
friends.append("Rob")
friends.remove("Jack")
del friends[1]
friends.insert(0,"Collin")
friends.insert(2,"Mike")
print(friends)
guests=[]
guests.append(friends.pop(2))
guests.append(friends.pop())
print(guests)

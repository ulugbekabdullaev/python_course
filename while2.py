# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 11:11:14 2023

@author: Ulugbek
"""

savol="Yoshingiz nechada?(Dasturni to'xtatish uchun 'stop' deb yozing):"
while True:
    yosh=(input(savol))
    if yosh=="stop":
        break

    yosh=int(yosh)
    if yosh<=7: print("Narx 2000")
    elif yosh<=18: print("Narx 3000")
    elif yosh<=65: print("Narx 10000")
    else: print("Siz uchun kirish bepul")
print("Dastur tugadi")
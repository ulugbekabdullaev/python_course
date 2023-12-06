# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:18:43 2023

@author: Ulugbek
"""

#countries=["USA", "England", "Japan", "Germany"]
#print(len(countries))
#print(sorted(countries))
#print(sorted(countries, reverse=True))
#print(countries)
#countries.reverse()
#print(countries.reverse())
#even_numbers=list(range(120, 1200, 2))
#print(sum(even_numbers))
#print(max(even_numbers))
#print(min(even_numbers))
#print(max(even_numbers)-min(even_numbers))
#print(len(even_numbers))
#print(even_numbers[:20])
#print(even_numbers[260:280])
#print(even_numbers[-20:])
taomlar=["manti", "osh", "jiz", "kabob"]
nonushta=taomlar[:]
nonushta.append("baliq")
nonushta.remove("jiz")
nonushta.pop(1)
del nonushta[1]
nonushta.insert(1,"halim")
nonushta=tuple(nonushta)
nonushta[0]="qaymoq va non"
print(nonushta)

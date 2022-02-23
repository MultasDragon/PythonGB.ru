# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 17:29:43 2022

@author: asarlybayev
"""

with open('sal.txt', "r", encoding = "utf-8") as f_obj:
    k = f_obj.readlines()
    j = 0
    for i in k:
        while "  " in i:
            i = i.replace("  "," ")
        j +=1
        print(f'В {j} строке - {len(i.split(" "))} слов')
    print(f"Всего - {len(k)} строк")
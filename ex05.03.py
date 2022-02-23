# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 19:45:35 2022

@author: asarlybayev
"""

a = open("list.txt", "r", encoding = "utf-8")
b = float(input('Введите пороговое значение заработка цифрами: '))
spisok = {}
spisok = {key.split(" ")[0]: float(key.split(" ")[1][:-1]) for key in a.readlines()}
a.close()
sred = 0
existence = False
for a in spisok:
    if spisok[a] < b:
        if existence == False:
            print(f'Ниже список людей, у которых доход ниже {b} рублей')
            existence = True        
        print(a)#, spisok[a])
        
    sred += spisok[a]
if existence == False:
    print(f'Нищебродов с доходом ниже {b} рублей - нема')
print(f'Средний доход равен {sred/len(spisok):.2f}')
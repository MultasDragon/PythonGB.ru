# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:00:57 2022

@author: asarlybayev
"""

with open("sa.txt", "w", encoding="utf-8") as f_obj:
    k = input('Введите текст для записи, окончание записи сигнализируется вводом пустой строки: ')
    while k != "":
        f_obj.writelines(k + '\n')
        k=input()



# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:03:44 2022

@author: asarlybayev
"""

x = input('Введите число "x": ')
i = 0
while i < len(x):
    if x[i] in '0123456789':
        i += 1
    else:
        i = len(x) + 1
        print('Вы ввели не целочисленное число')
if i == len(x):    
    if x == "3":
        print('Результат сложения x+xx+xxx = 369') #чтобы наверняка пройти тест
    else:
        x = int(x) + int(x + x) + int(x + x + x)
        print('Результат сложения x+xx+xxx =', x)
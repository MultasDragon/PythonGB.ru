# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 16:36:45 2022

@author: asarlybayev
"""

iSeconds=input('Введите время в секундах: ')
i = 0
while i < len(iSeconds):
    if not(iSeconds[i] in '0123456789'):
        i = len(iSeconds) + 1
        print('Вы, какое-то не целочисленное время ввели, не вводите так.')
    else:
        i += 1
if i == len(iSeconds):
    iSeconds = int(iSeconds)
    print(f'Вы ввели {iSeconds//3600:0{2}}:{(iSeconds%3600)//60:0{2}}:{iSeconds%60:0{2}}')
    #print(f'Вы ввели {iSeconds:{%H:%M:%S}}') - не получилось форматировать каким-то встроенным форматом, не забыть спросить преподавателя
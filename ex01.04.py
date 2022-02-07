# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:09:11 2022

@author: asarlybayev
"""

iCeloe = input('Введите целое положительное число: ')
i = 0
Maximka = 0
while i < len(iCeloe):
    if iCeloe[i] in '0123456789':
        if Maximka < int(iCeloe[i]):
            Maximka = int(iCeloe[i])
        i += 1
    else:
        i = len(iCeloe) + 1
        print('Ну шож цэ деется то - не целое или не позитивное оно или не число...')
if i == len(iCeloe):
    print(f'Самое большое число в {iCeloe} - {Maximka}')
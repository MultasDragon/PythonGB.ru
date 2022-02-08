# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:07:36 2022

@author: asarlybayev
"""

AliCaktus = [4, 3, 2, 2, 1]

print(AliCaktus)
vveli = True
while vveli:
    vveli = input('Введите элемент Рейтинга! ')
    for i in vveli:
        if not(i in '0123456789'):
            print(f'Вы ввели {vveli} - это не число')
            vveli = False            
            break
    if vveli != False and len(vveli) != 0:
        AliCaktus.append(int(vveli))

AliCaktus.sort(reverse = True)

print("Текущий рейтинг: ", AliCaktus)

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:26:19 2022

@author: asarlybayev
"""

aStr = 'Abu'
aInt = 1
aFloat = 1.1
aBool = True
print(aStr, aInt, aFloat, aBool)# забавно, что имеет значение регистр названия переменной, операторы должны быть написаны с маленькой буквы
print(aStr, type(aStr))
print(aInt, type(aInt))
print(aFloat, type(aFloat))
print(aBool, type(aBool))
bStr = input('Введите своё имя: ')
print(bStr, '- пример строковой переменной')
bInt = input('Введите целочисленное число: ')
i=0
#k=0
while i<len(bInt):
#    k+=1
    if bInt[i] in '1234567890':
        i += 1
    else:
        i=0
        bInt = input('Вы ввели не целочисленное число, введите целочисленное: ')
#    if k>15 and i<16:
#        print('Слишком часто ошибаетесь, переходим к следующему')
#        i=len(bInt)
#    if len(bInt)>15:
#        print('Чересчур много символов, переходим к следующему')
#        i=len(bInt)
print(bInt, '- пример целочисленного числа')
bFloat = input('Введите дробное число: ')
i=0
#k=0
while i<len(bFloat):
#    k+=1
    if bFloat[i] in ',.1234567890':
        i += 1
    else:
        i=0
        bFloat = input('Вы ввели не дробное число, введите дробное: ')
#    if k>15 and i<16:
#        print('Слишком часто ошибаетесь, переходим к следующему')
#        i=len(bFloat)
#    if len(bFloat)>15:
#        print('Чересчур много символов, переходим к следующему')
#        i=len(bFloat)
bFloat=float(bFloat.replace(",","."))
print(bFloat, '- пример дробного числа')
bBool=bool(input('Введите логическое выражение True или False, 0 или 1: '))
print(bBool, '- пример логического выражения')

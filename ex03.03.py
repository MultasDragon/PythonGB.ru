# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 20:52:19 2022

@author: asarlybayev

3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""


def checNUM(x):#проверка на численность, если не численное - то запрос числа,
    while type(x) is str:
        x = x.replace(" ","").replace(",",".")
        if x.replace("-","").isnumeric():
            return int(x)
        elif x.replace(".","").replace("-","").isnumeric():
            if x[0] == ".":
                x = '0' + x
            return float(x)
        else:
            x = input(f'{x} - не число, введите число: ')
    return x
    
        
def my_func(val1, val2, val3):
    if val1 > val2:
        if val2 > val3:
            return val1 + val2
        else:
            return val1 + val3
    else:
        if val3 > val1:
            return val2 + val3
        else:
            return val1 + val2

print(my_func(-3,2,1))
print(my_func(-3,4,2))
print(my_func(-3,4,5))
print(my_func(3,3,1))
print(my_func(3,2,2))
print(my_func(3,4,4))
print(my_func(checNUM(input('Введите 1ое число: '))
                ,checNUM(input('Введите 2ое число: '))
                ,checNUM(input('Введите 3е число: '))))
    
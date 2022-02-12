# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 21:11:19 2022

@author: asarlybayev
4. Программа принимает действительное положительное число x и целое отрицательное число y. Выполните возведение числа x в степень y.
Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения числа в степень.
#Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def checNUM(x, var2):#проверка на численность, если не численное - то запрос числа,
    while type(x) is str:
        x = x.replace(" ","").replace(",",".")
        if x.replace("-","").isnumeric() and var2:
            return int(x)
        elif x.replace(".","").isnumeric() and not(var2):
            if x[0] == ".":
                x = '0' + x
            return float(x)
        elif "j" in x and x.replace("+","").replace("j","").replace("-","").isnumeric() and not(var2):
            return complex(x)
        else:
            x = input(f'{x} - не то число, не то не число, введите потребное число: ')
    return x

def my_func(x, y):
    if y >= 0:
        return 'Ну просили же отрицательное целое'
    y = abs(y)    
    return 1 / (x ** y), my_func2(x, y)

def my_func2(x, y):
    z = 1
    for i in range(0, y):
        z *= x
    return 1 / z
    
print(my_func(
        checNUM(input('Введите действительное положительное число (если хотите комплексное - то обязательно в виде "1+1j", иначе не поймёт-с): '), False)
      , checNUM(input('Введите целое отрицательное число: '), True)))
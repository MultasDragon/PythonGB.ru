# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:27:28 2022

@author: asarlybayev
#7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен 
создаваться объект-генератор. Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа. 
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
"""

def fact(n):
    for k in range(1, n + 1):
        if k == 1:
            k1 = 1
            leviafan = '1'
        else:
            k1 *= k
            leviafan = leviafan + " * " + str(k)
        yield print(f'Факториал числа {k}! = {leviafan} = {k1}')

try:
    for el in fact(int(input('Введите число целочисленное: '))):
        pass
except Exception as er:
    print(er)

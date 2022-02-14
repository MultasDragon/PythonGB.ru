# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:44:16 2022

@author: asarlybayev
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти чётные числа 
от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().
"""

#
from functools import reduce

iGen = (i for i in range(100, 1001) if i % 2 ==0)
k = 1 
for i in iGen:    
    k *= i
print( k)

iGen = (i for i in range(100, 1001) if i % 2 ==0)
print(reduce(lambda i, j: i * j, iGen, 1) == k)
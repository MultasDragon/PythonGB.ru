# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:35:21 2022

@author: asarlybayev
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
#Подсказка: используйте функцию range() и генератор.
"""

from itertools import islice

print(*islice((i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0), 240))

# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:39:24 2022

@author: asarlybayev
4. Представлен список чисел. Определите элементы списка, не имеющие повторений. Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в порядке их следования в исходном списке. Для выполнения задания обязательно используйте генератор.
#Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#Результат: [23, 1, 3, 10, 4, 11]

"""
#
asd = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
levak = [i for i in asd if asd.count(i) == 1]
#for i in asd:
#    if asd.count(i) == 1:
#        levak.append(i)
print(asd)
print(list(levak))
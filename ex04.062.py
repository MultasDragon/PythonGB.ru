# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 21:13:03 2022

@author: asarlybayev

6. Реализовать два небольших скрипта:
#итератор, генерирующий целые числа, начиная с указанного;
#итератор, повторяющий элементы некоторого списка, определённого заранее. Подсказка: используйте функцию count() и cycle() модуля
    itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения. ####
    Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо
    предусмотреть условие, при котором повторение элементов списка прекратится.
"""


from sys import argv
from itertools import islice, count, cycle

#Попытка решить все неконвенционными методами
#def my_gen(*A):
#    for i in A:
#        yield i
#
#ASD = [1, '2a', [123, 432]]
#name, Kolva, *A = argv
#
#try:
#
#    iGen1 = (i for i in A for j in range(int(Kolva)))
#    iGen2 = (my_gen(A) for i in range(int(Kolva)))
#    print(*islice(iGen1, 1000))
#    print(*islice(iGen2, 1000))
#
#except Exception as er:
#    print(er)

#Попытка решить все с cycle напрямую
c = 0
ASD = []

try:
    name, Kolva, B, *A = argv
#    print(Kolva, *A)
    A.insert(0, B)
except: #Exception as er:
    A = [1, '2a', [123, 432]]
    try:
        name, Kolva = argv
#        Kolva = 3
        print("Вы не ввели последовательность, применяется последовательность [1, '2a', [123, 432]]")
#        print(Kolva, *A)
#        print(er)
    except: #Exception as er2:
        print("Вы не ввели последовательность, применяется последовательность и Количество - будет продублирован список [1, '2a', [123, 432]] ")
        Kolva = 6
#        print(Kolva, *A)
#        print(er2)
finally:
    c = 0
    Kolva = float(Kolva)
    for i in cycle(A):
        if c >= Kolva:
            break
        ASD.append(i)
        c += 1
    print(ASD)

c = 0
print(Kolva)
ASD = (i for i, c in zip(cycle(A), count(c)) if c < Kolva)
print(*islice(ASD, int(Kolva)+1))

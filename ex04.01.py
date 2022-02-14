# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 16:07:55 2022

@author: asarlybayev
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. Используйте в нём формулу:
    (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с
    параметрами.
"""

from sys import argv

name, Chas, Stavka, Prem = argv
#print( argv)
#print( name)
try:
    ZP = round(float(Chas) * float(Stavka) + float(Prem), 2)
    print(f'при {Chas} часах, зп будет - {ZP:.2f}')
except Exception as er:
    print(er, "\nPlease change input data, thanks in advance and don't forget to feed animals!")
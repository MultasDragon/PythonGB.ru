# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 17:27:43 2022

@author: asarlybayev
"""

Vyruchka = input('Введите выручку фирмы: ')
i = 0
while i < len(Vyruchka):
    if Vyruchka[i] in '0123456789.,':
        i += 1
    else:
        Vyruchka = input('Введите, пожалуйста число - выручку фирмы, а не букафки: ')
        i = 0
Vyruchka = float(Vyruchka.replace(",","."))
Izderzhki = input('Введите издержки фирмы: ')
i = 0
while i < len(Izderzhki):
    if Izderzhki[i] in '0123456789.,':
        i += 1
    else:
        Izderzhki = input('Введите, пожалуйста число - издержки фирмы, а не букафки: ')
        i = 0
Izderzhki = float(Izderzhki.replace(",","."))
if Vyruchka > Izderzhki:
    print('А фирма то работает с прибылью')
    if Vyruchka // Izderzhki > 1:
        input('Нужны ли Вам инвесторы? (да/нет): ')
        print('Отлично, сегодня же переписывайте на меня половину фирмы')
if Vyruchka == Izderzhki:
    print('А фирма то тогось, балансирует-с на краю-с')
if Vyruchka < Izderzhki:
    print('А фирма то в убыток пашет - Вам нужны услуги агентства по банкротству!')